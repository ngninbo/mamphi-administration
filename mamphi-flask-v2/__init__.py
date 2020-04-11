from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import os
import sys


db = SQLAlchemy()
DATABASE = 'sqlite:///database.db'


def create_app():

    if getattr(sys, 'frozen', False):
        template_folder = os.path.join(sys._MEIPASS, 'templates')
        static_folder = os.path.join(sys._MEIPASS, 'static')

        app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
    else:
        app = Flask(__name__)

    # config
    app.config.update(SECRET_KEY='secret_xxx')
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.init_app(app)

    # flask-login
    login_manager = LoginManager()
    login_manager.login_view = "login"
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def user_loader(user_id):
        return User.query.get(user_id)

    @login_manager.unauthorized_handler
    def unauthorized_handler():
        return '<p>Unauthorized</p>'

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app


def create_user(username, email, password):
    app = create_app()

    from werkzeug.security import generate_password_hash
    from .models import User

    with app.app_context():
        db.session.add(User(username=username, email=email,
                            password=generate_password_hash(password=password, method="sha256")))

        db.session.commit()

        print('user with name= {} has been created'.format(username))
