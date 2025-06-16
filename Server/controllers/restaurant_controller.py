from flask import Blueprint, jsonify, request, abort
from Server.app import db
from Server.models.restaurant import Restaurant


restaurant_bp = Blueprint('restaurants', __name__, url_prefix='/restaurants')



@restaurant_bp.route('', methods=['GET'])
def get_pizzas():
    restaurants = Restaurant.query.all()
    return jsonify([{
        "id": r.id,
        "name": r.name,
        "address": r.address

    } for r in restaurants]), 200


@restaurant_bp.route('/<int:id>', methods=['GET'])
def get_restaurant_bp():
    pass


@restaurant_bp.route('/<int:id>', methods=['DELETE'])
def delete_restaurant():
    pass