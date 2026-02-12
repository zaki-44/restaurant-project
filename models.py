# In this file we define our database tables
from database import db
from sqlalchemy import Date, Time, ForeignKey
from sqlalchemy.orm import relationship


class Client(db.Model):
    """Client model to store customer information"""
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50), nullable=False)
    prenom = db.Column(db.String(50), nullable=False)
    telephone = db.Column(db.String(15), nullable=False)
    
    # Relationship: one client can have multiple reservations
    reservations = relationship('Reservation', backref='client', lazy=True)
    
    def __repr__(self):
        return f"<Client {self.id} - {self.nom} {self.prenom}>"


class Reservation(db.Model):
    """Reservation model to store booking information"""
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(Date, nullable=False)
    heure = db.Column(Time, nullable=False)
    type_reservation = db.Column(db.String(50), nullable=False)
    nbr_person = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.String(200))
    
    # Foreign key to link reservation to a client
    client_id = db.Column(db.Integer, ForeignKey('client.id'), nullable=False)
    
    def __repr__(self):
        return f"<Reservation {self.id} - {self.type_reservation} on {self.date}>"
