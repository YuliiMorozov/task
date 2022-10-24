# from flask import render_template
# from flask_admin import Admin
# from flask_admin.contrib.sqla import ModelView
# from indication import app, db
# from models import House, Flat


# # @app.get('/admin')
# # def admin():
# #     return render_template('./admin.html')

# admin = Admin(app, name='Create house & flat', template_mode='bootstrap3')
# admin.add_view(ModelView(House, db.session, name='Add house number'))
# admin.add_view(ModelView(Flat, db.session, name='Add flat number'))