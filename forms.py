from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, TimeField,  DateField,SelectField,TextAreaField
from wtforms.validators import DataRequired, NumberRange,ValidationError,Length,Regexp
import datetime





def date_futur(form,field):
     if field.data< datetime.date.today():
        raise ValidationError("La date doit être dans le futur.")
     

class ReservationForm(FlaskForm):
     
     nom=StringField("Nom",validators=[DataRequired(),Length(min=1,max=10)])
     
     prenom=StringField("Prenom",validators=[DataRequired(),Length(min=1,max=10)])
     
     type_reservation= SelectField("Type de réservation", choices=[("VIP", "VIP"),("Fête privée", "Fête privée"),("à table", "À table")],validators=[DataRequired()])
      
     telephone = StringField("numéro de téléphone",validators= [DataRequired(), Regexp(r'^\d+$'),Length(min=5,max=15)])

     nbr=IntegerField("Nombre de personne",validators=[DataRequired(),NumberRange(min=1)] )

     jour=DateField("Veuillez choisir la date :  " ,format="%Y-%m-%d",validators=[DataRequired(),date_futur])

     heure=TimeField("Veuillez choisir l'heure de votre réservation :", format="%H:%M")
     
     notes = TextAreaField("Ajouter une remarque (optionnel)")
     submit=SubmitField("Reserver ")




