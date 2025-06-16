from Server.app import db


class Pizza(db.Model):
    __tablename__ = 'pizzas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.column(db.String, nullable=False)
    toppings = db.Column(db.String, nullable=False)