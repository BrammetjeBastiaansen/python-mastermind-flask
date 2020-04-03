from flask import request, redirect, render_template, url_for
from flask.views import MethodView


class Game_Controller(MethodView):
    def __init__(self, player_model, game_model):
        self._player_model = player_model
        self._game_model = game_model

    def get(self):
        if self._player_model.get_current_player is None:
            return redirect(url_for("main_bp.index"))
        elif self._game_model.current_game is None:
            return redirect(url_for("main_bp.new_game"))

        return render_template("game_screen.html",
                               game_sequence=self._game_model.game_colors,
                               amount_of_pins=self._game_model.current_game.position_amount)

    def post(self):
        pass
