# config/settings.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

db = SQLAlchemy()  # Initialize here but bind in create_app
migrate = Migrate()


def create_app(settings_conf=None):
    load_dotenv()

    app = Flask(__name__)
    os.environ.setdefault("FLASK_SETTINGS_MODULE", "config.dev")
    conf = settings_conf or os.getenv("FLASK_SETTINGS_MODULE")
    app.config.from_object(conf)

    # Register blueprints here
    from router.auth import auth_router
    from router.user import user_route
    from router.profile import profile_route

    app.register_blueprint(auth_router)
    app.register_blueprint(user_route)
    app.register_blueprint(profile_route)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    return app
