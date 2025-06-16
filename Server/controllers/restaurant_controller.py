from flask import Blueprint, jsonify, request, abort
from Server.app import db
from Server.models.restaurant import Restaurant


restaurant_bp = Blueprint('restaurants', __name__, url_prefix='/restaurants')

@restaurant_bp.route()
def get_pizzas():
    pass


@restaurant_bp.route()
def get_restaurant_bp():
    pass


@restaurant_bp.route()
def delete_restaurant():
    pass