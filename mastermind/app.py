# Imports
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_assets import Environment, Bundle


db = SQLAlchemy()


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config')
    app.config.from_pyfile(os.getcwd() + '/instance/config.py')

    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database/site.db?check_same_thread=False'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    with app.app_context():
        # Import parts of our application
        from mastermind.main import main_routes

        db.create_all()

        app.register_blueprint(main_routes.main_bp)

    assets = Environment(app)
    assets.url = app.static_url_path
    assets.debug = True

    scss = Bundle(
        'sass/app.scss',
        '../main/static/sass/main.scss',
        filters='pyscss',
        depends=['sass/**/*.scss', '../main/static/sass/**/*.scss'],
        output='gen/bundle.css'
    )

    js = Bundle(
        'js/app.js',
        '../main/static/js/app.js',
        filters='jsmin',
        depends=['js/**/*.js', '../main/static/js/**/*.js'],
        output='gen/bundle.js'
    )

    assets.register('scss_bundle', scss)
    assets.register('js_bundle', js)

    return app


if __name__ == '__main__':
    create_app().run(debug=True)
