from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy

# Globally accessible libraries
db = SQLAlchemy()


def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    db.init_app(app)
    app.config.from_object('config.Config')

    # Initialize Plugins
    db.init_app(app)

    with app.app_context():
        # Include our Routes
        from .user.user_routes import user_bp

        # Register Blueprints
        app.register_blueprint(user_bp)

        db.create_all()
        return app
