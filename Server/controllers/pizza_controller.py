from flask import Blueprint, jsonify
from Server.models.pizza import Pizza


pizza_bp = Blueprint('pizzas', __name__, url_prefix='/pizzas')


@pizza_bp.route()
def get_pizzas():
    pass