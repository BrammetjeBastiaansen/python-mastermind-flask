import json

from flask import request, redirect, render_template, url_for
from flask.views import MethodView


class Game_Controller(MethodView):
    def __init__(self, player_model, game_model):
        self._player_model = player_model
        self._game_model = game_model

    def get(self):
        if request.path == '/api/double_colors_enabled':
            return json.dumps({'double_colors_enabled': self._game_model.current_game.double_colors_allowed})

        if self._player_model.get_current_player is None:
            return redirect(url_for("main_bp.index"))
        elif self._game_model.current_game is None:
            return redirect(url_for("main_bp.new_game"))

        return render_template("game_screen.html",
                               game_sequence=self._game_model.game_sequence,
                               amount_of_pins=self._game_model.current_game.position_amount,
                               player_name=self._player_model.get_current_player.name,
                               cheat_enabled=self._game_model.current_game.cheats_used,
                               game_colors=self._game_model.game_colors)

    def post(self):
        dragged_colors = request.form.getlist("dragged")

        self._game_model.create_attempt(dragged_colors)

        # TODO: win check
        # All you have to do is call the set_pins_and_check_win method in game_model and send the result to the view as game_won
        # TODO: Pass data to redirect to show previous attempts on game screen.
        return redirect(url_for("main_bp.game"))
