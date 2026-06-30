from src.config import DB_CONFIG
from sqlalchemy import create_engine
from src.logger import logger

def load_to_postgres(df):

    logger.info(
        "Loading data int PostgreSQL"
    )

    connection_string = (
        f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}"
        f"@{DB_CONFIG['host']}:{DB_CONFIG['port']}"
        f"/{DB_CONFIG['database']}" )
    
    engine = create_engine(connection_string)

    df.to_sql(
        name = "weather_data",
        con = engine,
        if_exists ="append",
        index = False
    )

    logger.info(
        "Data loaded successfully"
    )