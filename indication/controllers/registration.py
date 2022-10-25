from flask import render_template, request, redirect, url_for, flash
from indication import db
from indication.forms import RegistrationForm
from indication.models import User
from flask_login import current_user


def create_registration():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
        
    registration_form = RegistrationForm()

    if registration_form.validate_on_submit():

        user = User(username=registration_form.username.data, email=registration_form.email.data)
        user.set_password(registration_form.password.data)

        user_check_in_db = User.query.filter_by(username=request.form['username']).first()
        email_check_in_db = User.query.filter_by(email=request.form['email']).first()  
          
        if user_check_in_db is None and email_check_in_db is None:
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login'))
        else:
            flash('This user or email is already registered') 
            return redirect(url_for('registration'))        
    return render_template("registration.html", title='Register', registration_form=registration_form)