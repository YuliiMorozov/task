from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_login import LoginManager
from flask_migrate import Migrate

app = Flask(__name__)

# This string is a way to protect against CSRF or cross-site document forgery.
app.config["SECRET_KEY"] = "my_secret"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mybase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)

# create login manager
login_manager = LoginManager()
login_manager.init_app(app)



from indication import urls
from indication.routes.home import *
from indication.routes.about import *
from indication.routes.registration import *
from indication.routes.create_payment import *
from indication.routes.payment import *
from indication.routes.login import *
from indication.routes.logout import *
from indication.routes.flat_house_id import *


from indication.routes.payment_routes.water import *
from indication.routes.payment_routes.gas import *
from indication.routes.payment_routes.electricity import *
from indication.routes.payment_routes.to_pay import *


from indication.api.routes.api_login import *
from indication.api.routes.api_home import *
from indication.api.routes.api_registration import *
from indication.api.routes.api_payment import *
from indication.api.routes.api_create_payment import *
from indication.api.routes.payment_flat_flat_id import *

db.create_all()