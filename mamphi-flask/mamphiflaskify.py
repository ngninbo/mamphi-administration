from fetcher.data_fetcher import MamphiDataFetcher
from flask import Flask, render_template, redirect, Response, request, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash  # generate_password_hash
import json
import os
import sys

# TODO Remove comments to export data from excel sheet to database if database not available
# data = MamphiData()
# data.export_data()
# db = data.db_filename

DATABASE = os.getcwd() + '/data/mamphi.db'  # db = "../" + data.db_filename
USER_DB = 'sqlite:///database.db'

fetcher = MamphiDataFetcher(mamphi_db=DATABASE)

db = SQLAlchemy()

if getattr(sys, 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS, 'templates')
    static_folder = os.path.join(sys._MEIPASS, 'static')
    app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
else:
    app = Flask(__name__)

# config
app.config.update(SECRET_KEY='secret_xxx')
app.config['SQLALCHEMY_DATABASE_URI'] = USER_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['DATABASE'] = DATABASE

db.init_app(app)

# flask-login
login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))


@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/login', methods=["POST"])
def login_post():
    email = request.form.get('username')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    if user is None:
        flash("Prüfen Sie bitte Ihre Anmeldedaten und versuchen Sie erneut.")

        return redirect(url_for('login'))

    elif user is not None and not check_password_hash(user.password, password=password):
        flash("Prüfen Sie bitte Ihre Anmeldedaten und versuchen Sie erneut.")

        return redirect(url_for('login'))

    login_user(user)

    return redirect(url_for('administration'))


@app.route('/mamphi/admin')
@login_required
def administration():
    return render_template("mamphi.html", name=current_user.username)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


# handle login failed
@app.errorhandler(401)
def page_not_found():
    return Response('<p>Login failed</p>')


@login_manager.unauthorized_handler
def unauthorized_handler():
    return '<p>Unauthorized</p>'


if __name__ == '__main__':
    import random
    import threading
    import webbrowser

    port = 5000 + random.randint(0, 999)
    url = "http://127.0.0.1:{0}".format(port)

    threading.Timer(1.25, lambda: webbrowser.open(url)).start()

    app.run(port=port, debug=False, host='0.0.0.0')
