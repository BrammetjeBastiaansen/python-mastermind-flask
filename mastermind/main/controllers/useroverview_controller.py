from flask import request, redirect, render_template
from flask.views import MethodView
from mastermind.main.models.player_model import Player_Model


class Useroverview_Controller(MethodView):
    def __init__(self):
        self._player_model = Player_Model()

    def get(self, id):
        return render_template("useroverview.html", player=self._player_model.get_player_by_id(id), game_amounts_by_date=self._player_model.get_played_game_amounts_by_date(id))
