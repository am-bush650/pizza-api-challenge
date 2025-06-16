from Server.app import db
from sqlalchemy.orm import validates




class RestaurantPizza(db.Model):
    __tablename__ = 'restaurant_pizzas' 


    #primary key — unique ID for each restaurant–pizza relationship
    id = db.Column(db.Integer, primary_key=True)
    #price of the pizza at a specific restaurant — must be provided (not NULL)
    price = db.Column(db.Integer, nullable=False)


    #foreign key — links this entry to a specific Restaurant
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)
    #foreign key — links this entry to a specific Pizza
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'), nullable=False)


    #this is a validation method for the 'price' field called whenever SQLAlchemy price is set.
    @validates('price')
    def validate_price(self, key, value):
        if not 1000 <= value < 2000:
            # If price is not between 1 (inclusive) and 30 (exclusive), raise an error.
            raise ValueError("Price must be between 1 and 30")
        return value