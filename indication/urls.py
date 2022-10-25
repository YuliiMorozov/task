from importlib.resources import read_text
from flask import render_template, request, redirect, url_for, flash, jsonify, request, make_response
from indication import app, db, login_manager
import indication
from .controllers import create_data, pay_information, water_information, gas_information, electricity_information, to_pay, create_registration, create_login
from indication.models.user import *
from indication.models.flat import *
from indication.models.house import *
import jwt
import datetime
from indication.forms import LoginForm
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
jwt = JWTManager(app)


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


@app.route("/apiapi/login", methods=["POST"])
def login_test():
    username = request.json.get("username", None)   
    password = request.json.get("password", None)   
    user = User.query.filter_by(username=username).first()

    if user is None:
        return jsonify({"msg": "Bad username or password"}), 401

    if username != user.username or user.check_password(password) is False:
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)



# @app.route('/api/login', methods=['GET','POST'])
# def login_api():
#     login_form = LoginForm()
    # print(login_form.email.data)
    # print(request.json)
    # print(request.headers)
    # print(request.query_string)
    # auth = request.headers.authorization
    # print(auth)

    # if not auth or not auth.username or not auth.password:
    #     return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required"'})
    # if request.method == "POST":
    #     print("email&password!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    #     email = request.form['email']        
    #     password = request.form['password']   

    #     user = User.query.filter_by(username=auth.username).first()
    #     user = User.query.filter_by(email=email).first()
    #     print(request.form)
    #     print("UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUSEEEEEEEEEEEEEEEEEEEEEEEEEEERRRR")
    #     print(user)
    # # if not user:
    #     return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required"'})

    # if check_password_hash(user.password, auth.password):
    #     token = jwt.encode({'email' : user.email, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])

    #     return jsonify({'token' : token.decode('UTF-8')})
    
    # return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required"'})


# @app.route("/login", methods=["POST"])
# def login():
#     username = request.json.get("username", None)
#     password = request.json.get("password", None)

#     user = User.query.filter_by(username=username).one_or_none()
#     if not user or not user.check_password(password):
#         return jsonify("Wrong username or password"), 401

#     # Notice that we are passing in the actual sqlalchemy user object here
#     access_token = create_access_token(identity=user)
#     return jsonify(access_token=access_token)








@app.route('/registration', methods=["POST"])
def registration():
    return create_registration()

# user loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route('/login', methods=['GET','POST'])
def login():
    return create_login()

@app.route('/')
@app.route('/home')
@login_required
def home():
    return render_template("index.html")

@app.route('/create_payment', methods=["GET", "POST"])
# @login_required
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
@app.route('/flat/<house_id>')
def flatbyhouse(house_id):
    flat = Flat.query.filter_by(house_id=house_id).all()
    flatArray = []
    for item in flat:
        flatObj = {}
        flatObj['id'] = item.id
        flatObj['flat_number'] = item.flat_number
        flatArray.append(flatObj)
    return jsonify({'flathouse' : flatArray})