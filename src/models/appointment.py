from src.app import db

class Appointment(db.Model):
    __tablename__ = "appointments"

    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.DateTime, nullable = False)
    reason = db.Column(db.String(200), nullable = False)
    status = db.Column(db.String(20), nullable = False)
    pet_id = db.Column(db.Integer, db.ForeignKey("pets.id"), nullable = False)
    vet_id = db.Column(db.Integer, db.ForeignKey("vets.id"), nullable = False)
