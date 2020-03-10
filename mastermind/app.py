# Imports
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config')
    app.config.from_pyfile(os.getcwd() + '/instance/config.py')

    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database/site.db'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    with app.app_context():
        # Import parts of our application
        from mastermind.main import main_routes

        db.create_all()

        app.register_blueprint(main_routes.main_bp)

    return app


if __name__ == '__main__':
    create_app().run(debug=True)
