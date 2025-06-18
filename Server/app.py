from dotenv import load_dotenv
load_dotenv

from flask import Flask
from .extensions import db, migrate
from .config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)

    @app.route('/')
    def restaurant():
        return f"welcome for the best pizza"


    #import Blueprints for different parts of the API (modular route structure)
    from Server.controllers.restaurant_controller import restaurant_bp
    from Server.controllers.pizza_controller import pizza_bp
    from Server.controllers.restaurant_pizza_controller import restaurant_pizza_bp


    #register each Blueprint with the app, so their routes become active
    app.register_blueprint(restaurant_bp)
    app.register_blueprint(pizza_bp)
    app.register_blueprint(restaurant_pizza_bp)


    #return the configured app instance
    return app

app = create_app()

