from flask import request, redirect, render_template, url_for
from flask.views import MethodView


class Game_Controller(MethodView):
    def __init__(self, player_model, game_model):
        self._player_model = player_model
        self._game_model = game_model

    def get(self):
        return render_template("game_screen.html", game_sequence=self._game_model.game_colors)

    def post(self):
        pass