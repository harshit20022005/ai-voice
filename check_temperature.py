import requests
import json
from voice import *



def get_temperature_openweathermap(city):
    api_key = "57750a40690b5a50f53cc755c386cfbc"  
    endpoint = "http://api.openweathermap.org/data/2.5/weather"

    response = requests.get(endpoint, params={"q": city, "appid": api_key, "units": "metric"})

    if response.status_code == 200:
        data = json.loads(response.text)

        if 'main' in data:
            temperature_celsius = data["main"]["temp"]
            return temperature_celsius
        else:
            print("Error: 'main' key not found in API response")
    else:
        print(f"Error: Failed to fetch data from API. Status code: {response.status_code}")

    return None


def Temp():
    city = "Harohalli, Karnataka"

    temperature_celsius = get_temperature_openweathermap(city)

    if temperature_celsius is not None:
        speechtx(f"The weather in {city} is {temperature_celsius}°C")
    else:
        print("Temperature data not available.")


