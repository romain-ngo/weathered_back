from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_cors import CORS

# Globally accessible libraries
db = SQLAlchemy()
mallow = Marshmallow()
bcrypt = Bcrypt()
jwt = JWTManager()
cors = CORS()


def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    # Initialize Plugins
    db.init_app(app)
    mallow.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    cors.init_app(app)

    with app.app_context():
        # Include routes
        from .user.user_routes import user_bp
        from .location.location_routes import location_bp

        # Register Blueprints
        app.register_blueprint(user_bp)
        app.register_blueprint(location_bp)

        db.create_all()
        return app
