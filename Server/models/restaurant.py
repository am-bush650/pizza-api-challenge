from Server.app import db #import the sqlalchemy instance

class Restaurant(db.model):
    __tablename__ = 'restaurants' #sets the table name in the db


    #primary key column - each restaurant will have a unique id
    id = db.Column(db.Integer, Primary_key=True)
    #name of restaurant cannot be null
    name = db.Column(db.String, nullable=False)
    #address of the restaurant cannot be null 
    address = db.Column(db.String, nullable=False) 


    restaurants_pizzas = db.relationship(
        'RestaurantPizza', #name of the related model (many to one rshp)
        backref='restaurant', #adds a '.restaurant' attribute on restaurantPizza instances 
        cascade='all, delete-orphan')#ensures if a restaurant is deleted its deleted with all its records from RestaurantPizza