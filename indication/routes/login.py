from indication import app, login_manager
from indication.models.user import User
from indication.controllers import create_login

# user loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route('/login', methods=['GET','POST'])
def login():
    return create_login()