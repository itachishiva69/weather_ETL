import requests
from src.config import API_KEY
from src.logger import logger

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def extract_weather(city):

    logger.info(f"Fetching weather data for {city}")

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(
        BASE_URL,
        params=params,
        timeout=10
    )

    if response.status_code == 404:

        logger.warning(
            f"City not found: {city}"
        )

        raise ValueError(
            f"City '{city}' not found"
        )

    response.raise_for_status()

    logger.info(
        f"Weather data fetched for {city}"
    )

    return response.json()