from flask import request, redirect, render_template, url_for
from flask.views import MethodView
from flask import after_this_request


class Game_Controller(MethodView):
    def __init__(self, player_model, game_model):
        self._player_model = player_model
        self._game_model = game_model

    def get(self):
        if self._player_model.get_current_player is None:
            return redirect(url_for("main_bp.index"))
        elif self._game_model.current_game is None:
            return redirect(url_for("main_bp.new_game"))

        @after_this_request
        def after_request_func(response):
            if self._game_model.has_won is not None:
                print("Resetting!")
                self._player_model.reset()
                self._game_model.reset()
            return response

        return render_template("game_screen.html",
                               game_sequence=self._game_model.get_current_game_sequence(),
                               amount_of_pins=self._game_model.current_game.position_amount,
                               player_name=self._player_model.get_current_player.name,
                               cheat_enabled=self._game_model.current_game.cheats_used,
                               game_colors=self._game_model.game_colors,
                               attempts=self._game_model.get_game_attempts(),
                               has_won=self._game_model.has_won)

    def post(self):
        dragged_colors = request.form.getlist("dragged")

        if len(dragged_colors) == self._game_model.current_game.position_amount:
            self._game_model.create_attempt(dragged_colors)
            self._game_model.set_pins_and_check_win()

        return redirect(url_for("main_bp.game"))
