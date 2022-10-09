from importlib.resources import read_text
from flask import render_template, request, redirect, url_for, flash
from indication import app, db, login_manager
from indication.views import create_data, pay_information, water_information, gas_information, electricity_information
from indication.forms.registration import RegistrationForm
from indication.forms.login import LoginForm
from indication.models.user import User

from flask_login import login_required, login_user, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash




@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")

@app.route('/create_payment', methods=["GET", "POST"])
def create_payment():
    return create_data()    

@app.route('/payment')
@login_required
def payment():
    return pay_information()

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



# user loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route('/registration', methods=["GET", "POST"])
def registration():
    registration_form = RegistrationForm()
    if registration_form.validate_on_submit():
        user = User(username=registration_form.username.data, email=registration_form.email.data)
        user.set_password(registration_form.password.data)
        db.session.add(user)
        db.session.commit()
    return render_template('registration.html', registration_form=registration_form)

@app.route('/login', methods=['GET','POST'])
def login():
  login_form = LoginForm()
  if login_form.validate_on_submit():

    user = User.query.filter_by(email=login_form.email.data).first()

    if user and user.check_password(login_form.password.data):

      login_user(user, remember=login_form.remember.data)
      next_page = request.args.get('next')
      return redirect(next_page) if next_page else redirect(url_for('home', _external=True, _scheme='https'))
    else:
      return redirect(url_for('login', _external=True, _scheme='https'))
  return render_template('login.html', login_form=login_form)



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









