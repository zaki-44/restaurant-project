@app.route('/reservation', methods=["GET", "POST"])
def reservation():
    form = ReservationForm()
    if form.validate_on_submit():
        new_reservation = Reservation(
            type_reservation=form.type_reservation.data,
            nbr_person=form.nbr.data,
            date=form.jour.data,
            heure=form.heure.data,
            notes=form.notes.data
        )
        new_client=Client(
            nom=form.nom.data,
            prenom=form.prenom.data,
            telephone=form.telephone.data,
        )

        db.session.add(new_reservation)
        db.session.add(new_client)
        db.session.commit()

        return render_template('merci.html')

    return render_template('reservation.html', form=form)