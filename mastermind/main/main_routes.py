from flask import Blueprint, render_template

main_bp = Blueprint('main_bp', __name__,
                    template_folder='templates',
                    static_folder='static')


@main_bp.route('/', methods=["GET"])
def index():
    return render_template("startscreen.html")

@main_bp.add_url_rule("/",)