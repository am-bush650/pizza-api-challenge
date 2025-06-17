from flask import Blueprint, request, jsonify
from Server.app import db
from Server.models.restaurant_pizza import RestaurantPizza #Import RestaurantPizza model
from Server.models.pizza import Pizza #Import Pizza model (used in response)
from Server.models.restaurant import Restaurant #Import Restaurant model (used in response)


restaurant_pizza_bp = Blueprint('restaurant_pizza', __name__, url_prefix='/restaurant_pizzas')

#route to create new restaurant_pizza
@restaurant_pizza_bp.route('', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json() # get JSON payload from client request
    try:
        
        pizza_chain = RestaurantPizza(
            price = data['price'],
            pizza_id = data['pizza_id'],
            restaurant_id = data['restaurant_id']
        )
        db.session.add(pizza_chain)
        db.session.commit()


        # return JSON response with details of the created record
        return jsonify({
            "id": pizza_chain.id,
            "price": pizza_chain.price,
            "pizza_id": pizza_chain.pizza.id,
            "restaurant_id":pizza_chain.restaurant.id,
            "pizza": {
                "id": pizza_chain.pizza.id,
                "name": pizza_chain.pizza.name,
                "toppings": pizza_chain.pizza.toppings
            },
            "restaurant": {
                "id": pizza_chain.restaurant.id,
                "name": pizza_chain.restaurant.name,
                "address": pizza_chain.restaurant.address
            }

        }), 201
    #handles any error that occurs during the process and returns a 400 Bad Request
    except Exception as e:
        return jsonify({"errors": [str(e)]}), 400

        
    

