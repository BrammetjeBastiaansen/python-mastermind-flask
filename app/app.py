import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET KEY'] = 'Exfe29yxyYWkc71p1cB/vQ=='
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///site.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

from models import Player, Game


@app.route('/')
def index():
    return "<h1>Test Page :ED</h1>"


if __name__ == '__main__':
    os.environ["FLASK_ENV"] = "development"
    app.run(debug=True)
