# Project: Online Closet Recommendation System 

## Description

This is a work-in-progress web application designed to help users decide what to wear based on the weather conditions in their city. By inputting their location, users receive clothing recommendations tailored to the temperature, rainfall, and wind conditions. The system uses a database of clothing items, each with an associated type, description, and image.

![alt text](<Screenshot 2025-01-10 at 9.04.32 PM.png>)

## Features

 - User Input: Users enter their city and country to get weather-based clothing recommendations.

 - Weather API Integration: The app fetches real-time weather data for the provided location.

 - Clothing Recommendation: Based on the weather, the app suggests appropriate clothing items from the database.

 - Dynamic Item Display: Displays the name, description, and image of the recommended items.

## Current Progress

 - Basic web interface using Flask and Jinja templates.

 - Weather data retrieval via gen_weather_stats function.

 - Clothing recommendation logic in find_conditions and choose_random functions.

 - Display of recommended items including description and image.

 - Functional database integration for storing and retrieving clothing items.

## Installation

Prerequisites: 

 - Python 3.8+

 - Flask

 - SQLAlchemy

 - A Weather API Key (e.g., OpenWeatherMap)

### Steps

Clone the repository:

```
git clone <repository_url>
cd online-closet
```

### Install dependencies:

`pip install -r requirements.txt`

Set up the database:

```
flask db init
flask db migrate
flask db upgrade
```

### Run the application:

``` flask run```

Access the app at http://127.0.0.1:5000.

## Usage

1. On the home screen, enter your city and country in the provided input field.

2. Submit the form to generate a recommendation.

3. View the recommended items along with their descriptions and images.

## Future Enhancements

- Improve the recommendation algorithm to include user preferences.

- Implement user authentication and personalized wardrobes.

- Allow users to upload their own clothing items to the database.

- Enhance the UI with better styling and responsive design.

- Add support for more weather conditions, such as snow or extreme heat.

