from extract import extract_weather
from transform import transform_weather
from load import load_to_postgres

def pipeline(city):

    raw_data = extract_weather(city)

    transformed = transform_weather(raw_data)

    load_to_postgres(transformed)

    return transformed


