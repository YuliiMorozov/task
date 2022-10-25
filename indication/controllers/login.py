from flask import render_template, request, redirect, url_for, flash
from indication.forms import LoginForm
from indication.models import User


from flask_login import current_user, login_user
# from werkzeug.security import generate_password_hash, check_password_hash


def create_login():
    # error = None
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    login_form = LoginForm()
    if login_form.validate_on_submit():
        
        user = User.query.filter_by(email=login_form.email.data).first()

        if user and user.check_password(login_form.password.data):

            login_user(user, remember=login_form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            # flash('Invalid credentials', 'error')
            return redirect(url_for('login'))
    return render_template('login.html', login_form=login_form)