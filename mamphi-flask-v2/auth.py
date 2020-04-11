from flask import Blueprint, render_template, redirect, url_for, request, flash, Response, session
from werkzeug.security import check_password_hash
from flask_login import login_user, login_required, logout_user
from .models import User


auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/login', methods=["POST"])
def login_post():
    email = request.form.get('username')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    if user is None:
        flash("Prüfen Sie bitte Ihre Anmeldedaten und versuchen Sie erneut.")

        return redirect(url_for('auth.login'))

    elif user is not None and not check_password_hash(user.password, password=password):
        flash("Prüfen Sie bitte Ihre Anmeldedaten und versuchen Sie erneut.")

        return redirect(url_for('auth.login'))

    login_user(user)

    return redirect(url_for('main.administration'))

# handle login failed
@auth.errorhandler(401)
def page_not_found():
    return Response('<p>Login failed</p>')


@auth.route('/logout')
@login_required
def logout():
    session.clear()
    logout_user()
    return redirect(url_for('auth.login'))
