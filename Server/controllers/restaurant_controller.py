from flask import Blueprint, jsonify
from ..extensions import db
from ..models.restaurant import Restaurant


restaurant_bp = Blueprint('restaurants', __name__, url_prefix='/restaurants')


# route to get all restaurants
@restaurant_bp.route('', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all() #query all restaurant records from the DB
    return jsonify([{
        "id": r.id,
        "name": r.name,
        "address": r.address

    } for r in restaurants]), 200 #return list of restaurant data as JSON


# route to get one restaurant by id with pizzas
@restaurant_bp.route('/<int:id>', methods=['GET'])
def get_restaurant_bp(id):
    restaurant = Restaurant.query.get(id) # fetch the restaurant by ID
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404 # Return 404 if not found
    return jsonify({
        "id": restaurant.id,
        "name": restaurant.name,
        "address": restaurant.address,
        "pizzas": [{
            "id": pizza_chain.pizza.id,
            "name": pizza_chain.pizza.name,
            "toppings": pizza_chain.pizza.toppings
        } for pizza_chain in restaurant.restaurant_pizzas]
    }), 200

# route to delete restaurant by id
@restaurant_bp.route('/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 400
    
    db.session.delete(restaurant)
    db.session.commit()
    return '', 204 #no content response