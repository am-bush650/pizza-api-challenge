from flask import Blueprint, request, jsonify
from Server.app import db
from Server.models.restaurant_pizza import RestaurantPizza
from Server.models.pizza import Pizza
from Server.models.restaurant import Restaurant


restaurant_pizza_bp = Blueprint('restaurant_pizza', __name__, url_prefix='/restaurant_pizzas')


@restaurant_pizza_bp.route('', methods=['POST'])
def create_restaurant_pizza():
    pass

