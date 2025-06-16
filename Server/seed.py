from Server.app import app, db
from Server.models.pizza import Pizza
from Server.models.restaurant import Restaurant
from Server.models.restaurant_pizza import RestaurantPizza
from faker import Faker
import random

faker = Faker()


with app.app_context():
    db.drop_all()
    db.create_all()


#create restaurants
restaurants = []
for _ in range(10): #create 10 restaurants
    restaurant = Restaurant(
        name=faker.company() + "Pizza",
        address = faker.address()
    )
    restaurants.append(restaurant)

db.session.add_all(restaurants)


#create pizzas
pizzas = []
toppings_list = ["Cheese", "Garlic", "Tomato", "Basil", "Mushroom", "Pepperoni", "Onion", "Olives"]

for _ in range(6): #create 6 pizzas
    toppings = ", ".join(faker.random_elements(elements=toppings_list, length=3, unique=True)) # 3 random ingredients
    pizza = Pizza(
        name = faker.first_name(), #fake pizza name
        toppings = toppings
    )
    pizzas.append(pizza)

    db.session.add_all(pizzas)
    db.session.commit() # all restaurants and pizzas have ids


#restaurant - pizza price relationships
restaurant_pizzas = []

for _ in range(16):
    pizza_chain = RestaurantPizza(
        price = random.randint(1000, 2000), #price between 100 and 2000
        pizza_id = random.choice(pizzas).id,
        restaurant_id = random.choice(restaurants).id
    )
    restaurant_pizzas.append(pizza_chain)

    db.session.add_all(restaurant_pizzas)
    db.session.commit(all)


