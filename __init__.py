from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_manager

db = SQLAlchemy
login_manager = LoginManager()

def create_app():
    # construct core application
    app = Flask(__name__, instance_relative_config=False)

    # application configuration
    app.config.from_object('config.Config')

    # initialise plugins
    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        from . import routes
        from . import auth
        from . import admins
        from . import products
        
        # register blueprints
        app.register_blueprint(auth.auth_bp)
        app.register_blueprint(routes.main_bp)
        app.register_blueprint(admins.admin_bp)
        app.register_blueprint(products.p_bp)

        # create database models
        db.create_all()

        return app

