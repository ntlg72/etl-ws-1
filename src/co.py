import pandas as pd
from sqlalchemy import create_engine

def insert_data(df, table_name, directory, db_url):
    """
    Inserta datos de un DataFrame en una base de datos SQL.

    :param df: DataFrame con los datos a insertar.
    :param table_name: Nombre de la tabla donde se insertarán los datos.
    :param directory: Directorio donde se encuentra la base de datos (si es SQLite).
    :param db_url: URL de conexión a la base de datos.
    """
    try:
        # Crear la conexión con la base de datos
        engine = create_engine(db_url)
        print("Conexión exitosa")

        # Insertar los datos
        df.to_sql(name=table_name, con=engine, if_exists='append', index=False)
        print(f"Datos insertados en la tabla '{table_name}' correctamente.")

    except Exception as e:
        print(f"❌ Error al insertar datos: {e}")

# Ejemplo de uso
df = pd.read_csv("datos.csv")  # Cargar un DataFrame de ejemplo
insert_data(df, "accidents", "ruta/al/directorio", "sqlite:///ruta/al/directorio/database.db")
