from extraction import extract_weather
from transform import transform_weather
from load import load_to_postgres

def pipeline():

    raw_data = extract_weather("chennai")

    transformed = transform_weather(raw_data)

    load_to_postgres(transformed)


    print("Pipeline finished")

if __name__ == "__main__":
    pipeline()