from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from ..models import House, Flat

class FormGeneral(FlaskForm):
    house = SelectField("Enter house number:", choices=[])    
    flat = SelectField("Enter the apartment number:", choices=[])
    water = StringField("Water meter readings:", render_kw={"placeholder": "00000.00"})
    gas = StringField("Gas meter readings:", render_kw={"placeholder": "00000.00"})
    electricity = StringField("Electricity meter readings:", render_kw={"placeholder": "00000.00"})
    submit = SubmitField("Send")