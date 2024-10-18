import requests

def fetch_weather_data(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    return response.json()  # Return the raw JSON data

def convert_to_celsius(kelvin_temp):
    return kelvin_temp - 273.15

def process_weather_data(weather_data):
    main_data = weather_data['main']
    temp_kelvin = main_data['temp']
    temp_celsius = convert_to_celsius(temp_kelvin)
    return {
        "temp": temp_celsius,
        "condition": weather_data['weather'][0]['main']
    }

def calculate_daily_aggregates(daily_data):
    temps = [data['temp'] for data in daily_data]
    return {
        "avg_temp": sum(temps) / len(temps),
        "max_temp": max(temps),
        "min_temp": min(temps)
    }

def check_thresholds(current_temp, threshold=35):
    if current_temp > threshold:
        print("Alert: Temperature exceeded!")
