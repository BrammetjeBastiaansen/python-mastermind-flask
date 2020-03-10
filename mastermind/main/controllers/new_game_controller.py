from flask import request, redirect, render_template
from flask.views import MethodView


class New_Game_Controller(MethodView):
    def __init__(self, player_model, game_model):
        self._player_model = player_model
        self._game_model = game_model

    def get(self):
        return render_template("create_new_game.html")
