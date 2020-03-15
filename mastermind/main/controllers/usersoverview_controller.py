from flask import request, redirect, render_template
from flask.views import MethodView
from mastermind.main.models.player_model import Player_Model


class Usersoverview_Controller(MethodView):
    def __init__(self):
        self._player_model = Player_Model()

    def get(self):
        return render_template("usersoverview.html", players=self._player_model.get_all_players())
