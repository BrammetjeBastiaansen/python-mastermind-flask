# Imports
from flask import Flask
import os

# Configs
app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile(os.getcwd() + '/instance/config.py')

with app.app_context():
    # Import parts of our application
    from mastermind.main import main_routes

    app.register_blueprint(main_routes.main_bp)

if __name__ == '__main__':
    app.run(debug=True)
