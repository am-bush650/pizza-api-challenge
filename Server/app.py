from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from .config import Config 

#initialize sqlalchemy and flask migrate
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)


    db.init_app(app)
    migrate.init_app(app, db)


    #import Blueprints for different parts of the API (modular route structure)
    from Server.controllers.restaurant_controller import restaurant_bp
    from Server.controllers.pizza_controller import pizza_bp
    from Server.controllers.restaurant_pizza_controller import create_restaurant_pizza


    #register each Blueprint with the app, so their routes become active
    app.register_blueprint(restaurant_bp)
    app.register_blueprint(pizza_bp)
    app.register_blueprint(create_restaurant_pizza)


    #return the configured app instance
    return app

app = create_app()
