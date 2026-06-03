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

st.set_page_config(
    page_title="Weather ETL Dashboard",
    layout="wide"
)

st.title("Weather ETL Dashboard")

city = st.text_input(
    "Enter City Name",
    value="Hyderabad"
)

if st.button("Fetch Weather"):

    if city.strip() == "":

        st.warning(
            "Please enter a city name."
        )

    else:

        try:

            pipeline(city)

            st.success(
                f"Weather data loaded for {city}"
            )

            st.rerun()

        except ValueError as e:

            st.warning(str(e))

        except Exception as e:

            st.error(
                "Something went wrong while fetching weather data."
            )

            st.write(str(e))

try:

    df = pd.read_sql(
        """
        SELECT *
        FROM weather_data
        ORDER BY timestamp DESC
        """,
        engine
    )

    if not df.empty:

        st.subheader("Weather Records")

        st.dataframe(
            df,
            use_container_width=True
        )

        latest = df.iloc[0]

        st.subheader("Latest Weather")

        col1, col2, col3, col4 = st.columns(4)

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

        with col4:
            st.metric(
                "Weather",
                latest["weather"]
            )

        st.subheader(
            "Temperature History"
        )

        st.line_chart(
            df.set_index("timestamp")[
                "temperature"
            ]
        )

        st.subheader(
            "Humidity History"
        )

        st.bar_chart(
            df.set_index("timestamp")[
                "humidity"
            ]
        )

    else:

        st.info(
            "No weather data available."
        )

except Exception:

    st.info(
        "No weather data available yet. Fetch a city first."
    )