import requests
from config import API_KEY

base_url = "https://api.openweathermap.org/data/2.5/weather"

def extract_weather(city="Mandapeta"):

    params = {
        "q" : city,
        "appid" : API_KEY,
        "units" : "metric"
    }

    response = requests.get(base_url, params=params)

    response.raise_for_status()

    return response.json()

