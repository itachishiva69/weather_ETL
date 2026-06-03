import pandas as pd
from datetime import datetime
from logger import logger


def transform_weather(data):

    logger.info(
        f"Transforming data for {data['name']}"
    )

    transformed = {
        "city" : data["name"],
        "temperature" : data["main"]["temp"],
        "humidity" : data["main"]["humidity"],
        "weather" : data["weather"][0]["main"],
        "wind_speed" : data["wind"]["speed"],
        "timestamp" : datetime.now().strftime("%Y-%m-%d %I:%M %p")
    }

    logger.info("Transformation completed")
    return pd.DataFrame([transformed])