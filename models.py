
#in this file we define our tables 
from database import db
from sqlalchemy import Date,Time





class Reservation(db.Model):                    # une table =  class  
 id =db.Column(db.Integer,primary_key=True)
 date = db.Column(Date,nullable=False)
 heure = db.Column(Time,nullable=False)
 type_reservation = db.Column(db.String(50), nullable=False)
 nbr_person=db.Column(db.Integer,nullable=False)
 notes=db.Column(db.String(100))


 def __repr__(self):
    return f"<Reservation {self.id} - {self.type_reservation}>"

 


class Client(db.Model):
    id =db.Column(db.Integer,primary_key=True)
    nom = db.Column(db.String(10), nullable=False)    
    prenom = db.Column(db.String(10), nullable=False)   
    telephone = db.Column(db.String(10),nullable=False)
 
    def __repr__(self):
        return f"<Client {self.id} - {self.nom}>"
