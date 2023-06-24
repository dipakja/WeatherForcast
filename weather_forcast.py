import requests
import json

API_KEY = 'c00600c8e3d8d1bcaa1c396e27d30c76'
API_URL = 'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
def get_weather_forecast(city):
    url = API_URL.format(city=city, api_key=API_KEY)
    response = requests.get(url)

    if response.status_code == 200:
        data = json.loads(response.text)
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']

        print(f"Weather forecast for {city}:")
        print(f"- Description: {weather}")
        print(f"- Temperature: {temperature} celsius")
        print(f"- Humidity: {humidity}%")
    elif response.status_code == 404:
        print(f"Error: City '{city}' not found.")
    else:
        print("An error occurred while fetching weather data.")

# Get the city name from user input
city_name = input("Enter a city name: ")

# Call the function with the provided city name
get_weather_forecast(city_name)
