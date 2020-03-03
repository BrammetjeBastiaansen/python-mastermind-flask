import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///site.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)



@app.route('/')
def hello_world():
    return 'HELLO WORLD!'


if __name__ == '__main__':
    os.environ["FLASK_ENV"] = "development"
    app.run(debug=True)
