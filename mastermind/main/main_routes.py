from flask import Blueprint
from .controllers.player_controller import Player_Controller
from .controllers.usersoverview_controller import Usersoverview_Controller
from .controllers.useroverview_controller import Useroverview_Controller
from .controllers.game_controller import Game_Controller
from .controllers.new_game_controller import New_Game_Controller
from mastermind.main.models.player_model import Player_Model
from mastermind.main.models.game_model import Game_Model
from .services.game_service import Game_Service
from .services.player_service import Player_Service

main_bp = Blueprint('main_bp', __name__,
                    template_folder='templates',
                    static_folder='static',
                    static_url_path='/main/static')

# Services
player_service = Player_Service()
game_service = Game_Service()

# Models
# We declare the models here and pass them to the our MethodView controller.
# The reason for this is because there is no cleaner way to do this using MethodView.
# It's still better then having a messy and un-maintainable router.

player_model = Player_Model(player_service)
game_model = Game_Model(game_service)


# Routes
# We use add_url_rule to declare routes instead of the @route decorator.
# The reason for this is that we use MethodView for our controllers and
# these do not support the route decorator.

main_bp.add_url_rule("/", view_func=Player_Controller.as_view("index", player_model), methods=["GET"])
main_bp.add_url_rule("/", view_func=Player_Controller.as_view("create", player_model), methods=["POST"])

main_bp.add_url_rule("/new-game", view_func=New_Game_Controller.as_view("new_game", player_model, game_model), methods=["GET"])
main_bp.add_url_rule("/new-game", view_func=New_Game_Controller.as_view("new_game_create", player_model, game_model), methods=["POST"])

main_bp.add_url_rule("/game", view_func=Game_Controller.as_view("game", player_model, game_model), methods=["GET"])
main_bp.add_url_rule("/game", view_func=Game_Controller.as_view("game_update", player_model, game_model), methods=["POST"])

main_bp.add_url_rule("/users-overview", view_func=Usersoverview_Controller.as_view("users_overview", player_model, game_model), methods=["GET"])
main_bp.add_url_rule("/user-overview/<id>", view_func=Useroverview_Controller.as_view("user_overview", player_model, game_model), methods=["GET"])
