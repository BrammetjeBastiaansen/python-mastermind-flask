from flask import request, redirect, render_template, url_for
from flask.views import MethodView


class New_Game_Controller(MethodView):
    def __init__(self, player_model, game_model):
        self._player_model = player_model
        self._game_model = game_model

    def get(self):
        if self._player_model.get_current_player is None:
            return redirect(url_for("main_bp.index"))

        return render_template("create_new_game.html")

    def post(self):
        request_data = request.form

        double_colors_allowed = int(request_data["doubleColorOption"]) == 1
        cheat_mode_allowed = int(request_data["cheatModeOption"]) == 1
        amount_of_colors = int(request_data["amountOfColorsOption"])
        amount_of_pins = int(request_data["amountOfPins"])

        if not double_colors_allowed and amount_of_colors < amount_of_pins:
            return redirect(url_for("main_bp.new_game"))

        self._game_model.create_new_game(self._player_model.get_current_player.id, double_colors_allowed,
                                         cheat_mode_allowed, amount_of_colors, amount_of_pins)

        return redirect(url_for("main_bp.game"))
