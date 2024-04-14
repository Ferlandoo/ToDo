from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from .config.config_app import Config
from .config.create_db import create_database

db = SQLAlchemy(engine_options={"pool_pre_ping": True})

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    create_database()
    db.init_app(app)

    from .models import User
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    with app.app_context():
        from .auth import auth as auth_blueprint
        from .main import main as main_blueprint
        app.register_blueprint(auth_blueprint)
        app.register_blueprint(main_blueprint)
        db.create_all()
    return app
