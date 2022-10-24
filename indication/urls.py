from importlib.resources import read_text
from flask import render_template, request, redirect, url_for, flash, jsonify, request, make_response
from indication import app, db, login_manager
from .controllers import create_data, pay_information, water_information, gas_information, electricity_information, to_pay
from .forms import LoginForm, RegistrationForm
from indication.models.user import *
from indication.models.flat import *
from indication.models.house import *

from flask_login import current_user, login_required, login_user, logout_user
# from werkzeug.security import generate_password_hash, check_password_hash

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

# @app.get('/admin')
# def admin():
#     return render_template('admin.html')

admin = Admin(app, name='Create house & flat', template_mode='bootstrap3')
admin.add_view(ModelView(House, db.session, name='Add house number'))
admin.add_view(ModelView(Flat, db.session, name='Add flat number'))




@app.route('/registration', methods=["GET", "POST"])
def registration():

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




# user loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/login', methods=['GET','POST'])
def login():

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








@app.route('/')
@app.route('/home')
@login_required
def home():
    return render_template("index.html")

@app.route('/create_payment', methods=["GET", "POST"])
@login_required
def create_payment():
    return create_data()    

@app.route('/payment')
@login_required
def payment():
    return pay_information()

@app.route('/payment/<float:sum>')
@login_required
def item_buy(sum):
    return to_pay()

@app.route('/payment/water')
def water():
    return water_information()

@app.route('/payment/gas')
def gas():
    return gas_information()

@app.route('/payment/electricity')
def electricity():
    return electricity_information()

@app.route('/about')
def about():
    return render_template("about.html")

# a decorator here to handle unauthorized users:
@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('login'))





@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))



# @app.after_request
# def redirect_to_signin(response):
#     if response.status_code == 401:
#         return redirect(url_for('login') + '?next=' + request.url)

#     return response




# create a json 
@app.route('/flat/<get_flat>')
def flatbyhouse(get_flat):
    flat = Flat.query.filter_by(house_id=get_flat).all()
    flatArray = []
    for item in flat:
        flatObj = {}
        flatObj['id'] = item.id
        flatObj['flat_number'] = item.flat_number
        flatArray.append(flatObj)
    return jsonify({'flathouse' : flatArray})