# Weather ETL Dashboard

## Overview

Weather ETL Dashboard is a beginner-friendly Data Engineering project built with Python, PostgreSQL, and Streamlit.

The application allows users to enter a city name, fetch real-time weather data from the OpenWeatherMap API, transform the data into a structured format, store it in PostgreSQL, and visualize historical weather records through an interactive Streamlit dashboard.

The project follows the ETL (Extract, Transform, Load) process and includes logging and error handling.

---

## Features

* Extract weather data from OpenWeatherMap API
* Transform JSON data into a structured format
* Load data into PostgreSQL
* Interactive Streamlit dashboard
* Real-time weather data collection
* Historical weather data storage
* Temperature trend visualization
* Humidity trend visualization
* Application logging
* Error handling for invalid city names and API failures
* Environment variable management using `.env`

---

## ETL Workflow

```text
User Input (City Name)
           ↓
     Streamlit UI
           ↓
      Extract Data
           ↓
     Transform Data
           ↓
    Load to PostgreSQL
           ↓
 Display Dashboard
           ↓
 Logging & Monitoring
```

---

## Project Structure

```text
weather_etl/

│
├── logs/
│   └── pipeline.log
│
├── .env
├── config.py
├── logger.py
├── extract.py
├── transform.py
├── load.py
├── pipeline.py
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Technologies Used

* Python
* Streamlit
* PostgreSQL
* SQLAlchemy
* Pandas
* Requests
* Python Dotenv
* OpenWeatherMap API

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/itachishiva69/weather_ETL.git
cd weather_etl
```

### Create a Virtual Environment

```bash
python -m venv myenv
```

### Activate the Virtual Environment

Windows:

```bash
myenv\Scripts\activate
```

Linux/Mac:

```bash
source myenv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Weather API Setup

### Create an OpenWeatherMap Account

1. Visit https://openweathermap.org/api
2. Create a free account.
3. Verify your email address.
4. Log in to your account.

### Generate an API Key

1. Navigate to the API Keys section.
2. Create a new API key.
3. Copy the generated API key.

Example:

```text
1234567890abcdef1234567890abcdef
```

**Note:** New API keys may take a few minutes to become active.

---

## PostgreSQL Database Setup

Before running the application, PostgreSQL must be installed and running on your system.

Connect to PostgreSQL:

```bash
psql -U postgres
```

Create the database:

```sql
CREATE DATABASE weather_db;
```

Verify the database exists:

```sql
\l
```

Connect to the database:

```sql
\c weather_db
```

### Important Note

The application **does not create the PostgreSQL database automatically**.

You must manually create the `weather_db` database before running the application.

The application **does automatically create the `weather_data` table** when weather data is inserted for the first time.

| Component           | Created Automatically |
| ------------------- | --------------------- |
| PostgreSQL Server   | No                    |
| weather_db Database | No                    |
| weather_data Table  | Yes                   |
| Weather Records     | Yes                   |

---

## Configuration

Create a `.env` file in the project root directory.

```env
API_KEY=your_api_key_here

DB_HOST=localhost
DB_PORT=5432
DB_NAME=weather_db
DB_USER=postgres
DB_PASSWORD=your_password
```

Replace the values with your own credentials.

---

## Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

Streamlit will start a local server and open the dashboard in your browser.

Example:

```text
Local URL: http://localhost:8501
```

---

## Using the Application

1. Enter a city name.
2. Click **Fetch Weather**.
3. The application will:

   * Fetch weather data from OpenWeatherMap.
   * Transform the API response.
   * Store the data in PostgreSQL.
   * Update the dashboard automatically.
4. View:

   * Weather records table
   * Latest weather metrics
   * Temperature history chart
   * Humidity history chart

---

## Database Schema

After the `weather_db` database has been created manually, the application automatically creates the `weather_data` table when the first weather record is inserted.

Table: `weather_data`

| Column      | Type      |
| ----------- | --------- |
| city        | VARCHAR   |
| temperature | FLOAT     |
| humidity    | INTEGER   |
| weather     | VARCHAR   |
| wind_speed  | FLOAT     |
| timestamp   | TIMESTAMP |

---

## Logging

Application logs are stored in:

```text
logs/pipeline.log
```

Example:

```text
2026-06-03 16:30:00 | INFO | Pipeline started for Hyderabad
2026-06-03 16:30:01 | INFO | Weather data fetched for Hyderabad
2026-06-03 16:30:02 | INFO | Data loaded successfully
```

---

## Error Handling

The application handles:

* Invalid city names
* Network connection issues
* API request failures
* Database insertion failures
* Empty city input

Example:

```text
City 'asdfghjkl' not found
```

---

## Future Improvements

* Scheduled weather collection
* Docker support
* Airflow orchestration
* Cloud deployment
* Weather forecasting endpoints
* User authentication
* Multiple weather providers
* Data quality validation

---

## Learning Outcomes

This project demonstrates:

* ETL Fundamentals
* REST API Integration
* Data Transformation
* PostgreSQL Integration
* Streamlit Dashboard Development
* Logging
* Error Handling
* Environment Variable Management
* Data Visualization

---

## Author

Built as a hands-on Data Engineering project for learning ETL pipelines, PostgreSQL integration, and dashboard development using Streamlit.

---

## .gitignore

Create a `.gitignore` file to prevent sensitive or unnecessary files from being uploaded to GitHub.

```gitignore
myenv/
.env
__pycache__/
*.pyc
logs/
.vscode/
.idea/
```
