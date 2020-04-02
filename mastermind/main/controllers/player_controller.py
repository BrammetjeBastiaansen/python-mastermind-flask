from flask import request, redirect, render_template
from flask.views import MethodView


class Player_Controller(MethodView):
    def __init__(self, player_model):
        self._player_model = player_model

    def get(self):
        return render_template("startscreen.html")

    def post(self):
        playerName = request.form["playerName"]

        if len(playerName) < 2:
            return redirect("/")

        if not self._player_model.get_existing_player(playerName):
            self._player_model.create_new_player(playerName)

        self._player_model.set_current_player = self._player_model.get_existing_player(playerName)

        return redirect("/new-game")
