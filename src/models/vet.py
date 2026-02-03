from src.app import db

class Vet(db.Model):
    __tablename__ = "vets"
    
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(20), nullable = False)
    last_name = db.Column(db.String(30), nullable = False)
    email = db.Column(db.String(30), unique = True, nullable = False)
    phone = db.Column(db.String(20))
    specialty = db.Column(db.String(50))
