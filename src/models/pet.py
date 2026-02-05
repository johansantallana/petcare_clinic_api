from src.app import db

class Pet(db.Model):
    __tablename__ = "pets"
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), nullable = False)
    species = db.Column(db.String(20), nullable = False)
    breed = db.Column(db.String(20), nullable = False)
    age = db.Column(db.Integer)
    owner_id = db.Column(db.Integer, db.ForeignKey("owners.id"), nullable = False)
    
    appointments = db.relationship("Appointment", backref = "pet", cascade="all, delete-orphan")