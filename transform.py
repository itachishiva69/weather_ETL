import pandas as pd
from datetime import datetime


def transform_weather(data):

    transformed = {
        "city" : data["name"],
        "temperature" : data["main"]["temp"],
        "humidity" : data["main"]["humidity"],
        "weather" : data["weather"][0]["main"],
        "wind_speed" : data["wind"]["speed"],
        "timestamp" : datetime.now().strftime("%Y-%m-%d %I:%M %p")
    }

    return pd.DataFrame([transformed])