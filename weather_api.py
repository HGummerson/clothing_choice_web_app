import requests 
import json
from config import WEATHER_API_KEY

def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}'
    response = requests.get(url)
    weather_data = response.json()
    return weather_data