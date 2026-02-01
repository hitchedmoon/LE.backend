from flask import Flask
from config import Config  # Import the class directly
from .extensions import db, migrate, ma

def create_app():
    app = Flask(__name__)
    
    # Load config directly from the class object
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

    # Use a deferred import for blueprints to avoid circular issues
    from .routes.user_routes import user_bp
    app.register_blueprint(user_bp, url_prefix='/users')

    with app.app_context():
        from .models.user import User
        from .models.ticket import Ticket

    return app