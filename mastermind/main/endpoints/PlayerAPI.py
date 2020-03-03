from flask import Flask, make_response, jsonify, request, redirect, url_for, render_template
from flask.views import MethodView
from models import Player, Game


class PlayerAPI(MethodView):
    def __init__(self):
        pass

    def get(self):
        return render_template("startscreen.html")

    def post(self):
        print("true")
        return "Player.select()"
