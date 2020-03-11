from flask import request, redirect, render_template, url_for
from flask.views import MethodView


class New_Game_Controller(MethodView):
    def __init__(self, player_model, game_model):
        self._player_model = player_model
        self._game_model = game_model

    def get(self):
        return render_template("create_new_game.html")

    def post(self):
        print(request.form)
        # return redirect(url_for("main_bp.new_game_create"))
        pass