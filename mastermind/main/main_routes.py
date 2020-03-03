from flask import Blueprint, render_template
from .endpoints.PlayerAPI import PlayerAPI

main_bp = Blueprint('main_bp', __name__,
                    template_folder='templates',
                    static_folder='static')


# Routes
main_bp.add_url_rule("/", view_func=PlayerAPI.as_view("index"), methods=["GET"])
main_bp.add_url_rule("/create", view_func=PlayerAPI.as_view("create"), methods=["POST"])
