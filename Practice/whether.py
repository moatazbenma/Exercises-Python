import os
import requests

def main():
    api_key = '75590b616c6995b9e339fd554f04fb05'
    city = input("Enter a city name: ")
    weather_data = get_weather(city, api_key)
    display_weather(weather_data)

def get_weather(city, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)  # Send GET request to the API
    response.raise_for_status()  # Raise an error for bad status codes
    return response.json()  # Convert the JSON response into a Python dictionary

def display_weather(data):
    if data:
        # Extract values from the data
        city = data.get('name')
        country = data.get('sys', {}).get('country')
        temp = data.get('main', {}).get('temp')
        # Note: The correct key is "humidity", not "humudity"
        humidity = data.get('main', {}).get('humidity')
        
        # 'weather' is a list, so we access the first item and then its description.
        weather_list = data.get('weather', [])
        if weather_list:
            weather_description = weather_list[0].get('description')
        else:
            weather_description = "No description available"
        
        # Display the data nicely
        print(f"Weather in {city}, {country}:")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {weather_description.capitalize()}")
    else:
        print("No weather data available.")


main()
