from extract import extract_weather
from transform import transform_weather
from load import load_to_postgres
from logger import logger


def pipeline(city):

    try:

        logger.info(
            f"Pipeline started for {city}"
        )

        raw_data = extract_weather(city)

        transformed_data = transform_weather(
            raw_data
        )

        load_to_postgres(
            transformed_data
        )

        logger.info(
            f"Pipeline completed for {city}"
        )

        return transformed_data

    except Exception as e:

        logger.error(
            f"Pipeline failed for {city}: {e}"
        )

        raise