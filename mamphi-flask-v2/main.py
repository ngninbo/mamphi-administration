from flask import Blueprint, render_template
from flask_login import login_required, current_user


main = Blueprint('main', __name__)


@main.route("/")
def index():
    return render_template("index.html")


@main.route('/mamphi/admin')
@login_required
def administration():
    return render_template("mamphi.html", name=current_user.username)
