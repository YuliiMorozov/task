from importlib.resources import read_text
from flask import render_template, request, redirect, url_for, flash
from indication import app, db
from .controllers import create_data, pay_information, water_information, gas_information, electricity_information, to_pay
from .forms import LoginForm, RegistrationForm
from indication.models.user import *

from flask_login import LoginManager, login_required, login_user, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

# create login manager
login_manager = LoginManager()
login_manager.init_app(app)

@app.route('/registration', methods=["GET", "POST"])
def registration():
    registration_form = RegistrationForm()
    if request.method == "POST":

        username = request.form['username']
        email = request.form['email']
                 
        user = User.query.filter_by(username=username, email=email).first()    
        if user is None:
            user = User(username=username, email=email)   
            user.set_password(registration_form.password.data)     
            db.session.add(user)
        try:            
            db.session.commit()
            return redirect('/registration')
        except:
            return "Error! Make sure the forms are filled out correctly."
    else:
        return render_template("registration.html",
                                registration_form=registration_form)




    # if registration_form.validate_on_submit():
    #     username = request.form['username']
    #     email = request.form['email']
    #     user = User.query.filter_by(username=username, email=email).first()
    #     if user is None:
    #         user = User(username=registration_form.username.data, email=registration_form.email.data)
    #         user.set_password(registration_form.password.data)
    #         db.session.add(user)
    #         db.session.commit()
    # return render_template('registration.html', registration_form=registration_form)



# user loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/')
@app.route('/login', methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():

        user = User.query.filter_by(email=login_form.email.data).first()

        if user and user.check_password(login_form.password.data):

            login_user(user, remember=login_form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            return redirect(url_for('login'))
    return render_template('login.html', login_form=login_form)














# @app.route('/')
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



# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     login_form = LoginForm()
#     login = request.form.get('login')
#     password = request.form.get('password')

#     if login and password:
#         user = User.query.filter_by(login=login).first()
        
#         if check_password_hash(user.password, password):
#             login_user(user)

#             next_page = request.arg.get('next')

#             redirect(next_page)
#         else:
#             flash('Login or password is not correct')

#     else:
#         flash('Please fill login and password fields')

#         return render_template('login.html', login_form=login_form)


# @app.route('/registration', methods=['GET', 'POST'])
# def registration():

#     registration_form = RegistrationForm()
#     login = request.form.get('login')
#     password = request.form.get('password')
#     password2 = request.form.get('password2')

#     if request.method == 'POST':
#         if not (login or password or password2):
#             flash('Please, fill all fields!')
#         elif password != password2:
#             flash('Passwords are not equal!')
#         else:
#             hash_psw = generate_password_hash(password)
#             user = User(login=login, password=hash_psw)
#             db.session.add(user)
#             db.session.commit()

#             return redirect(url_for('login'))

#             return render_template('login.html', registration_form=registration_form)


# @app.route('/logout', methods=['GET', 'POST'])
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('home'))

# @app.after_request
# def redirect_to_signin(response):
#     if response.status_code == 401:
#         return redirect(url_for('login') + '?next=' + request.url)

#     return response




# login loader
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     login_form = LoginForm()
#     if login_form.validate_on_submit():        
#         user = User.query.filter_by(email=login_form.email.data).first()
#         if user and user.check_password(login_form.password.data):
#             login_user(user, remember=login_form.remember.data)
#             next_page = request.args.get('next')
#             return redirect(next_page) if next_page else redirect(url_for('home', _external=True, _scheme='https'))
#         else:
#             return redirect(url_for('login', _external=True, _scheme='https'))
#     return render_template('login.html', login_form=login_form)
