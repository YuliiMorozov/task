from importlib.resources import read_text
from flask import jsonify
from indication import app, db


from indication.models.user import *
from indication.models.flat import *
from indication.models.house import *


app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
# jwt = JWTManager(app)



from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

# @app.get('/admin')
# def admin():
#     return render_template('admin.html')

admin = Admin(app, name='Create house & flat', template_mode='bootstrap3')
admin.add_view(ModelView(House, db.session, name='Add house number'))
admin.add_view(ModelView(Flat, db.session, name='Add flat number'))



@app.route('/api/<username_id>')
def user(username_id):
    user = User.query.filter_by(id=username_id).all()
    userArray = []
    for item in user:
        userObj = {}
        userObj['id'] = item.id
        userObj['username'] = item.username
        userObj['email'] = item.email
        userObj['password_hash'] = item.password_hash
        userObj['joined_at'] = item.joined_at
        userArray.append(userObj)
    return jsonify({'USERS' : userArray})