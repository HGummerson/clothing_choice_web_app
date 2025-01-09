from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class WeatherForm(FlaskForm):
    city = StringField('City,country', render_kw={'placeholder': 'Enter your city'})
    submit = SubmitField('Get Weather')