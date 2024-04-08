from flask import Flask
from .models import db, login_manager
from .auth import auth as auth_blueprint
from .main import main as main_blueprint
from .config import Config
from .create_db import create_database

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        create_database()
        app.register_blueprint(auth_blueprint)
        app.register_blueprint(main_blueprint)
        db.create_all()
    return app
