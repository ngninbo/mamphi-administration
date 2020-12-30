from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user


main = Blueprint('main', __name__)


@main.route("/")
def index():
    return redirect(url_for('auth.login'))


@main.route('/mamphi/admin')
@login_required
def administration():
    return render_template("mamphi.html", name=current_user.username)
