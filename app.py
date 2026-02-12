import os
from flask import Flask, render_template, redirect, url_for, jsonify
from datetime import date
from database import db
from forms import ReservationForm
from models import Reservation,Client



app=Flask(__name__)
app.config['SECRET_KEY']=os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get('DATABASE_URL', 'sqlite:///amine.db')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app) # link db with  our app



    


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/menu')
def menu():
  return render_template('menu.html')

@app.route('/contact')
def contact():
    return render_template('contact.html') 

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/reservation', methods=["GET", "POST"])
def reservation():
    form = ReservationForm()
    if form.validate_on_submit():
        # First create the client
        new_client = Client(
            nom=form.nom.data,
            prenom=form.prenom.data,
            telephone=form.telephone.data,
        )
        db.session.add(new_client)
        db.session.flush()  # Generate the client.id before creating reservation
        
        # Then create the reservation linked to the client
        new_reservation = Reservation(
            type_reservation=form.type_reservation.data,
            nbr_person=form.nbr.data,
            date=form.jour.data,
            heure=form.heure.data,
            notes=form.notes.data,
            client_id=new_client.id  # Link to the client
        )
        
        db.session.add(new_reservation)
        db.session.commit()

        return render_template('merci.html')

    return render_template('reservation.html', form=form)



# @app.route("/books")
# def show_books():
#     books = Book.query.all()
#     return "<br>".join([f"{b.id} - {b.title} ({b.pages} pages)" for b in books]) mnb3d nutilisiwha bach ndisplayy l serveur les reservation t3 lyoum


if __name__=='__main__':
    with app.app_context():
        db.create_all()  # Create tables if they don't exist
    app.run(debug=True)
else:
    # For production deployment (Render, Heroku, etc.)
    with app.app_context():
        db.create_all()  # Create tables if they don't exist