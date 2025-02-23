import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
import pandas as pd

def get_db_connection():
    load_dotenv()
    user = os.getenv('MYSQL_USER')
    password = os.getenv('MYSQL_PASSWORD')
    host = os.getenv('MYSQL_HOST')
    port = os.getenv('MYSQL_PORT')
    dbname = os.getenv('MYSQL_DB')
    db_url = f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{dbname}"

    try:
        engine = create_engine(db_url)
        connection = engine.connect()
        print("Connected to the database successfully")
        return connection
    except Exception as e:
        print(f"Error: {e}")
        return None

def read_candidates_table(connection):
    query = "SELECT * FROM candidates"
    return pd.read_sql(query, connection)
