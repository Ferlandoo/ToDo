from flask import Flask
from .models import db, login_manager
from .routes import auth as auth_blueprint
from .routes import main as main_blueprint
from .config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        app.register_blueprint(auth_blueprint)
        app.register_blueprint(main_blueprint)
        db.create_all()
    return app
