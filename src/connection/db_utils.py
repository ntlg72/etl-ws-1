import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
import pandas as pd
import psycopg2

def get_db_connection():
    load_dotenv()
    user = os.getenv('PG_USER')
    password = os.getenv('PG_PASSWORD')
    host = os.getenv('PG_HOST')
    port = os.getenv('PG_PORT')
    dbname = os.getenv('PG_DATABASE')

    db_url = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}"

    try:
        engine = create_engine(db_url)
        connection = engine.connect()
        print("Connected to the database successfully")
        return connection
    except Exception as e:
        print(f"Error: {e}")
        return None