import os

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'HELLO WORLD!'


if __name__ == '__main__':
    os.environ["FLASK_ENV"] = "development"
    app.run(debug=True)
