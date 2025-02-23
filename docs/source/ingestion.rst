Data Ingestion
--------------

The process conducted in this section involves reading the *candidates.csv* dataset, and transforming it into a Pandas DataFrame  for later storage in a database.


Establishing the Database Connection
""""""""""""""""""""""""""""""""""""

To establish a connection to the MySQL database, environment variables are loaded from the .env file, which securely stores database credentials. The sqlalchemy library's ``create_engine`` function is used to create a database engine instance, which facilitates the connection to the MySQL database. This approach ensures that the database credentials are not hard-coded into the script, enhancing security.