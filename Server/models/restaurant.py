from Server.app import db

class Restaurant(db.model):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, Primary_key=True)
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)