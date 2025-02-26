Para mostrar solo el número de batch cuando ocurra un error, puedes ajustar el bloque `except` en tu función. Aquí tienes una versión mejorada del código:

```python
def insert_data(df, table_name, batch_size=1000):
    """
    Inserts data from DataFrame to DB in MySQL in batches.

    :param df: DataFrame with data to insert.
    :param table_name: Name of the table where data is supposed to be inserted.
    :param batch_size: Number of rows to insert per batch.
    """
    engine = get_engine()
    connection = engine.connect()
    transaction = connection.begin()
    print("Successful connection.")

    try:
        for i in range(0, len(df), batch_size):
            batch_df = df.iloc[i:i + batch_size]
            batch_df.to_sql(name=table_name, con=connection, if_exists='append', index=False)
            print(f"Inserted batch {i // batch_size + 1} successfully.")

        transaction.commit()
        print(f"All data inserted into '{table_name}' successfully.")
    
    except Exception as e:
        batch_number = i // batch_size + 1
        transaction.rollback()
        print(f"Error in batch {batch_number}: {e}")
    
    finally:
        connection.close()

insert_data(df, "candidates")
```

En esta versión, he agregado una variable `batch_number` dentro del bloque `except` para capturar y mostrar el número del batch que causó el error. Ahora, si ocurre un error, se imprimirá un mensaje que indica en qué batch ocurrió el problema.
