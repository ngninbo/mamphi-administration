from flask import Flask, render_template, redirect, Response, request, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash


db = SQLAlchemy()
app = Flask(__name__)
# config
app.config.update(SECRET_KEY='secret_xxx')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

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


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/login', methods=["POST"])
def login_post():
    email = request.form.get('useremail')
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
    return redirect(url_for('index'))


# handle login failed
@app.errorhandler(401)
def page_not_found():
    return Response('<p>Login failed</p>')


@login_manager.unauthorized_handler
def unauthorized_handler():
    return '<p>Unauthorized</p>'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
