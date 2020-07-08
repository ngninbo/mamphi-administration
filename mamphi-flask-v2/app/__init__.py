from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
DATABASE_URI = 'sqlite:///database.db'


def create_app():

    app = Flask(__name__)

    # config
    app.config.update(SECRET_KEY='secret_xxx')
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
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
