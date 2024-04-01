from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from structure.auth.routes import auth as auth_blueprint
from structure.main.routes import main as main_blueprint
from database import db

class Config:
    SECRET_KEY = '479cdcf08d2b4a16b9c3ea2eba2853a7'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost:3306/todo_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        app.register_blueprint(auth_blueprint)
        app.register_blueprint(main_blueprint)
        return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=5018)
