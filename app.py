import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

from pipeline import pipeline

load_dotenv()

engine = create_engine(
    f"postgresql://{os.getenv('DB_USER')}:"
    f"{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}:"
    f"{os.getenv('DB_PORT')}/"
    f"{os.getenv('DB_NAME')}"
)

st.title("Weather ETL Dashboard")

city = st.text_input(
    "Enter City Name",
    value="Hyderabad"
)

if st.button("Fetch Weather"):

    pipeline(city)

    st.success(
        f"Weather data for {city} loaded successfully!"
    )

try:

    df = pd.read_sql(
        """
        SELECT *
        FROM weather_data
        ORDER BY timestamp DESC
        """,
        engine
    )

    st.subheader("Weather Data")

    st.dataframe(df)

    if not df.empty:

        latest = df.iloc[0]

        st.subheader("Latest Record")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "City",
                latest["city"]
            )

        with col2:
            st.metric(
                "Temperature",
                f"{latest['temperature']} °C"
            )

        with col3:
            st.metric(
                "Humidity",
                f"{latest['humidity']} %"
            )

        st.subheader("Temperature History")

        st.line_chart(
            df.set_index("timestamp")["temperature"]
        )

        st.subheader("Humidity History")

        st.bar_chart(
            df.set_index("timestamp")["humidity"]
        )

except Exception:

    st.info(
        "No weather data available yet. Fetch a city first."
    )