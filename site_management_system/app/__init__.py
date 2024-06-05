from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_socketio import SocketIO
from flask_mail import Mail
from flask_migrate import Migrate
from site_management_system.config import Config

db = SQLAlchemy()
login_manager = LoginManager()
socketio = SocketIO()
mail = Mail()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    socketio.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)

    from site_management_system.app.routes import bp as auth_bp
    app.register_blueprint(auth_bp)

    return app








