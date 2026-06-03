# Weather ETL Pipeline

## Overview

This project is a basic ETL (Extract, Transform, Load) pipeline built with Python and the OpenWeatherMap API.

The pipeline retrieves weather data for a city, transforms the raw API response into a structured format, and loads the result into a PostgreSQL database.

This project was created to learn the fundamentals of Data Engineering and ETL workflows.

---

## ETL Flow

```text
Weather API
    ↓
Extract
    ↓
Transform
    ↓
Load to PostgreSQL
```

---

## Project Structure

```text
weather_etl/

│
├── .env
├── config.py
├── extract.py
├── transform.py
├── load.py
├── pipeline.py
├── requirements.txt
└── README.md
```

---

## Technologies Used

* Python
* Requests
* Pandas
* PostgreSQL
* SQLAlchemy
* Python Dotenv
* OpenWeatherMap API

---

## Installation

### Clone the Repository

```bash
git clone <repository-url>
cd weather_etl
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux/Mac**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install requests pandas python-dotenv sqlalchemy psycopg2-binary
```

### Save Dependencies

```bash
pip freeze > requirements.txt
```

---

## Weather API Setup

This project uses the OpenWeatherMap API to retrieve weather data.

### Create an OpenWeatherMap Account

1. Visit OpenWeatherMap.
2. Create a free account.
3. Verify your email address.
4. Log in to your account.

### Generate an API Key

1. Open the API Keys section.
2. Create a new API key.
3. Copy the generated API key.

Example:

```text
1234567890abcdef1234567890abcdef
```

**Note:** Newly created API keys may take a few minutes to become active.

---

## PostgreSQL Database Setup

Before running the pipeline, create the PostgreSQL database.

### Connect to PostgreSQL

```bash
psql -U postgres
```

### Create the Database

```sql
CREATE DATABASE weather_db;
```

### Verify the Database Exists

```sql
\l
```

### Connect to the Database

```sql
\c weather_db
```

The ETL pipeline will automatically create the `weather_data` table when it runs for the first time.

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

Replace:

* `your_api_key_here` with your OpenWeatherMap API key.
* `your_password` with your PostgreSQL password.

---

## Pipeline Components

### Extract

Retrieves weather data from the OpenWeatherMap API.

Example fields collected:

* City Name
* Temperature
* Humidity
* Weather Condition
* Wind Speed

---

### Transform

Processes the raw JSON response and converts it into a structured Pandas DataFrame.

Example output:

| city      | temperature | humidity | weather |
| --------- | ----------- | -------- | ------- |
| Hyderabad | 32          | 60       | Clouds  |

---

### Load

Loads the transformed data into PostgreSQL.

Table Name:

```sql
weather_data
```

The table is automatically created if it does not already exist.

---

## Running the Pipeline

Run the pipeline:

```bash
python pipeline.py
```

---

## Expected Result

After successful execution:

* Weather data is fetched from the API.
* Data is transformed into a structured format.
* PostgreSQL table `weather_data` is created automatically.
* Weather records are inserted into the database.

Verify the data:

```sql
SELECT * FROM weather_data;
```

---

## Learning Outcomes

By building this project, you will learn:

* ETL Fundamentals
* REST API Integration
* JSON Processing
* Data Transformation
* Pandas DataFrames
* PostgreSQL Integration
* Environment Variables
* Python Project Organization

---

## Future Improvements

* Add logging
* Add exception handling
* Support multiple cities
* Export data to CSV
* Schedule automatic execution
* Dockerize the application
* Integrate Apache Airflow
* Deploy to the cloud

---

## Author

Weather ETL Pipeline built as a beginner Data Engineering project using Python, PostgreSQL, and the OpenWeatherMap API.
