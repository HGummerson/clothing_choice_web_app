from flask import Flask, render_template, request, redirect, url_for
from config import WEATHER_API_KEY
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db,Item
from forms import WeatherForm
import json
import os
import requests

# app configuration
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = os.path.join('static','uploads')

db.init_app(app)
migrate = Migrate(app,db)

@app.route('/')
def index():
    items = Item.query.all()
    return render_template('index.html',items=items)

@app.route('/upload', methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        description = request.form.get('description')
        clothingtype = request.form.get('clothingtype')
        colour = request.form.get('colour')

        if 'file' in request.files:
            file = request.files['file']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)
                new_item = Item(description=description, file_name=file.filename, clothingtype=clothingtype, colour=colour)
                db.session.add(new_item)
                db.session.commit()
                return redirect(url_for('index'))
            
        return 'No file provided.'
    return render_template('upload.html')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'jpg', 'jpeg', 'png', 'gif'}

@app.route('/delete/<int:item_id>', methods=['GET'])
def delete_item(item_id):
    item = Item.query.get(item_id)

    if item:
        db.session.delete(item)
        db.session.commit()

    return redirect(url_for('index'))

@app.route('/weather', methods=['GET','POST'])
def weather():
    form = WeatherForm()

    if form.validate_on_submit():
        city = form.city.data
        weather_data = get_weather(city)
    
        if weather_data is None :
            return 'error fetching data'
        
        temperature_c = round(weather_data['main']['temp'] - 273.15, 2)
        feels_like_c = round(weather_data['main']['feels_like'] - 273.15, 2)
        temp_min_c = round(weather_data['main']['temp_min'] - 273.15, 2)
        temp_max_c = round(weather_data['main']['temp_max'] - 273.15, 2)
        rain = weather_data['weather'][0]['description']
        wind = weather_data['wind']['speed']
       
        return render_template('weather.html',form=form, temperature_c=temperature_c,
                           feels_like_c=feels_like_c,
                           temp_min_c=temp_min_c,
                           temp_max_c=temp_max_c, rain=rain, wind=wind)
    return render_template('weather.html',form=form)

def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}'
    response = requests.get(url)
    weather_data = response.json()
    return weather_data

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)