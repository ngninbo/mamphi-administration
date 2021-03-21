from fetcher.data_fetcher import MamphiDataFetcher
from flask import Flask, render_template, redirect, Response, request, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
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
app.config['DATABASE'] = DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)

# flask-login
login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(64), unique=True)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password, method="sha256")

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)


@app.route('/')
def welcome():
    return render_template("welcome.html")


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

    elif user is not None and not user.verify_password(password=password):
        flash("Prüfen Sie bitte Ihre Anmeldedaten und versuchen Sie erneut.")

        return redirect(url_for('login'))

    login_user(user)

    return redirect(url_for('description'))


@app.route("/mamphi/description")
@login_required
def description():
    return render_template("description.html", name=current_user.username)


@app.route("/mamphi/center%list")
@login_required
def center():
    zentren = fetcher.fetch_center()
    return render_template("center.html", zentren=zentren, name=current_user.username)


@app.route("/mamphi/patient%consent")
@login_required
def consent():
    consents = fetcher.fetch_consent()
    incomplete_consents = fetcher.fetch_consent_list(consent="incomplete")
    missing_consents = fetcher.fetch_consent_list(consent="missing")
    consents_after_randomization = fetcher.fetch_consent_list(consent=None)

    options = [
        {'text': "Bitte Liste auswählen", 'value': None},
        {'text': "Vollstandige Liste der Einwilligungen", 'value': 1},
        {'text': "Liste der fehlenden Einwilligungen", 'value': 2},
        {'text': "Liste der unvollständigen Einwillungen", 'value': 3},
        {'text': "Liste der verspätete Einwilligungen", 'value': 4}
    ]

    return render_template("consent.html", consents=consents, incomplete_consents=incomplete_consents,
                           missing_consents=missing_consents, consents_after_randomization=consents_after_randomization,
                           options=options, name=current_user.username)


@app.route("/mamphi/randomisation%week=1")
@login_required
def random_w_1():
    results = fetcher.fetch_rand_week(week=1)

    return render_template("random_w_1.html", results=results, name=current_user.username)


@app.route("/mamphi/randomisation%week=2")
@login_required
def random_w_2():
    results = fetcher.fetch_rand_week(week=2)

    return render_template("random_w_2.html", results=results, name=current_user.username)


@app.route("/mamphi/monitor/planing")
@login_required
def monitoring():
    results = fetcher.retrieve_monitoring_plan()

    return render_template("monitorplan.html", monitoringplan=results, name=current_user.username)


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
