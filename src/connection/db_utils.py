from dotenv import load_dotenv
import os
from sqlalchemy import create_engine

def get_connection():
    load_dotenv()
    user = os.getenv('PG_USER')
    password = os.getenv('PG_PASSWORD')
    host = os.getenv('PG_HOST')
    port = os.getenv('PG_PORT')
    dbname = os.getenv('PG_DATABASE')

    
    db_url = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}"

    try:
        engine = create_engine(db_url)
        print("Engine created succesfully")
        return engine
    except Exception as e:
        print(f"Error: {e}")
        return None


def close_connection(engine):
    if engine:
        try:
            engine.dispose()
            print("Engine connection closed.")
        except Exception as e:
            print(f"Error closing connection: {e}")
    else:
        print("No engine to close.")
