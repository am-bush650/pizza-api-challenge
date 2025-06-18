from flask import Blueprint, jsonify
from ..extensions import db
from ..models.pizza import Pizza # importing the pizza model



pizza_bp = Blueprint('pizzas', __name__, url_prefix='/pizzas')


@pizza_bp.route('', methods=['GET']) # route handler for GET requests to '/pizzas'
def get_pizzas():

    #fetch all pizza records from the database
    pizzas = Pizza.query.all() 

    return jsonify([{
        "id":p.id, #return each pizza's id
        "name": p.name, #return each pizza's name
        "toppings": p.toppings

    # return the list as JSON with HTTP 200 OK
    } for p in pizzas]), 200 