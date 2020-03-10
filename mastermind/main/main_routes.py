from flask import Blueprint
from .controllers.player_controller import Player_Controller
from .controllers.usersoverview_controller import Usersoverview_Controller
from .controllers.useroverview_controller import Useroverview_Controller
from .controllers.new_game_controller import New_Game_Controller
from mastermind.main.models.player_model import Player_Model
from mastermind.main.models.game_model import Game_Model


main_bp = Blueprint('main_bp', __name__,
                    template_folder='templates',
                    static_folder='static')

# Models
player_model = Player_Model()
game_model = Game_Model()

# Routes
main_bp.add_url_rule("/", view_func=Player_Controller.as_view("index", player_model), methods=["GET"])
main_bp.add_url_rule("/", view_func=Player_Controller.as_view("create", player_model), methods=["POST"])

main_bp.add_url_rule("/new-game", view_func=New_Game_Controller.as_view("new_game", player_model, game_model), methods=["GET"])

main_bp.add_url_rule("/usersoverview", view_func=Usersoverview_Controller.as_view("usersoverview"), methods=["GET"])
main_bp.add_url_rule("/useroverview", view_func=Useroverview_Controller.as_view("useroverview"), methods=["GET"])
