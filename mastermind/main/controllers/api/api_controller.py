from flask import request, redirect, render_template, url_for, jsonify
from flask.views import MethodView


class Api_Controller(MethodView):
    def __init__(self, player_model, game_model):
        self._player_model = player_model
        self._game_model = game_model

    def get(self):
        if request.path == '/api/game/data':
            if self._game_model.current_game:
                return jsonify(double_colors_enabled=self._game_model.current_game.double_colors_allowed,
                               amount_of_positions=self._game_model.current_game.position_amount)

        return self.__return_default()

    @classmethod
    def __return_default(cls):
        return jsonify(None)
