# Pizza Restaurant Api

```
A RESTful API for managing restaurants, pizzas, and the relationships between them.
Built with Flask using the MVC pattern, PostgreSQL, SQLAlchemy ORM, and Flask-Migrate.

```

```
pizza-api-challenge/
├── Server/
│ ├── app.py # App setup and blueprint registration
│ ├── config.py # DB config
│ ├── extensions.py # db & migrate init
│ ├── seed.py # Database seed file
│ ├── models/
│ │ ├── init.py
│ │ ├── pizza.py
│ │ ├── restaurant.py
│ │ └── restaurant_pizza.py
│ ├── controllers/
│ │ ├── init.py
│ │ ├── pizza_controller.py
│ │ ├── restaurant_controller.py
│ │ └── restaurant_pizza_controller.py
├── migrations/
├── .env # Contains DATABASE_URL
|── PIZZA API.postman_collection.json
├── Pipfile
└── README.md

```

# Dependancies

pipenv install
flask flask_sqlalchemy
flask_migrate
python-dotenv
pipenv shell

## Configure environment variables

create a .env file in the project root

## Initialize database

export FLASK_APP=Server/app.py
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

## Seeding the database

python -m Server.seed

This will recreate and populate the database with mock restaurants, pizzas and restaurant-pizza relationships using faker

## Running the app

flask run

## Route summary

### GET / restaurants

Returns all restaurants
http://127.0.0.1:5000/restaurants

### GET / restaurants / <id>

Returns a single restaurant and its pizzas
http://127.0.0.1:5000/restaurants/1

### Get / pizzas

Returns all pizzas
http://127.0.0.1:5000/pizzas

### POST / restaurant_pizzas

Creates a new restaurant- pizza relationship

## Example requests and responses

```
== Get / restaurants

json

[
  {
    "address": "89229 Johnson Track Suite 449\nSouth Markport, IL 35337",
    "id": 1,
    "name": "Fields LLCPizza"
  },
  {
    "address": "986 Wang Mall Apt. 606\nNew Kathleenberg, ND 89649",
    "id": 2,
    "name": "Riley, Moore and OrtegaPizza"
  },
  ...
]

```

```

== Get / restaurants/1

json

{
  "address": "89229 Johnson Track Suite 449\nSouth Markport, IL 35337",
  "id": 1,
  "name": "Fields LLCPizza",
  "pizzas": [
    {
      "id": 3,
      "name": "Gregory",
      "toppings": "Tomato, Mushroom, Pepperoni"
    },
    {
      "id": 2,
      "name": "Christopher",
      "toppings": "Pepperoni, Onion, Basil"
    }
  ]
}

if not found

{ "error": "Restaurant not found" }

```

```
== DELETE / restaurant/1
Success:
204 No Content

if not found:

json

{ "error": "Restaurant not found" }

```

```
== GET / pizzas

json

[
  {
    "id": 1,
    "name": "Antonio",
    "toppings": "Pepperoni, Olives, Tomato"
  },
  {
    "id": 2,
    "name": "Christopher",
    "toppings": "Pepperoni, Onion, Basil"
  },
  {
    "id": 3,
    "name": "Gregory",
    "toppings": "Tomato, Mushroom, Pepperoni"
  },
  ...
]

```

```
== POST / restaurant_pizzas

Request:

json

{
  "price": 1500,
  "pizza_id": 1,
  "restaurant_id": 2
}

Response:

json

{
    "id": 17,
    "pizza": {
        "id": 1,
        "name": "Antonio",
        "toppings": "Pepperoni, Olives, Tomato"
    },
    "pizza_id": 1,
    "price": 1500,
    "restaurant": {
        "address": "986 Wang Mall Apt. 606\nNew Kathleenberg, ND 89649",
        "id": 2,
        "name": "Riley, Moore and OrtegaPizza"
    },
    "restaurant_id": 2
}

Validation error(400)

{"erors": ["Price must be between 1000 and 2000]}

```

## Validation Rules

To ensures that data entered is correct, safe, and in the expected format

```
== Model - level validations

Handled using SQLACHEMY and its @validates decorator

RestaurantPizza Model

-------------------------------------------------------------------

@validates('price')
def validate_price(self, key, value):
    if not 1000 <= value < 2000:
        raise ValueError("Price must be between 1000 and 2000")
    return value
-------------------------------------------------------------------
enforce rule - price must be within 1000 and 1999
value outside this range raises an error
```

```
== Database constraints via sqlalchemy columns

nullable=False

Restaurant

-------------------------------------------------------------------
name = db.Column(db.String, nullable=False)
address = db.Column(db.String, nullable=False)
-------------------------------------------------------------------
enforced rule - name and address cannot be null

pizza
-------------------------------------------------------------------
name = db.Column(db.String, nullable=False)
toppings = db.Column(db.String, nullable=False)
-------------------------------------------------------------------
enforced rule - name and toppings

RestaurantPizza
-------------------------------------------------------------------
price = db.Column(db.Integer, nullable=False)
restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)
pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'), nullable=False)
-------------------------------------------------------------------
enforced rule - price, restaurant_id and pizza_id are all required cannot be null

```

```
== Cascade delete validation

Restaurant model

-------------------------------------------------------------------
restaurants_pizzas = db.relationship(
    'RestaurantPizza',
    backref='restaurant',
    cascade='all, delete-orphan'
)
-------------------------------------------------------------------
enforced rule - Deleting a Restaurant automatically deletes all associated RestaurantPizza records (orphan cleanup).

```

## Postman collection

- create a new collection
- add requests

Get = Get all restaurants - http://127.0.0.1:5000/restaurants

GET = Get single restaurants by id - http://127.0.0.1:5000/restaurants/1

DELETE = Delete restaurants by Id - http://127.0.0.1:5000/restaurants/1

GET = Get all pizzas - http://127.0.0.1:5000/pizzas

POST = Create RestaurantPizza - http://127.0.0.1:5000/restaurant_pizza

- save the collection
- export save as...

```
export FLASK_APP=Server/app.py
export FLASK_ENV=development

seeding the db
python -m Server.seed - to reset

```
