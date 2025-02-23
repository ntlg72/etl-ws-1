
Workshop - 001
=============================

By **Natalia López Gallego**



Overview
--------

This project involves efficient data management and advanced visualization techniques. Starting with a CSV file containing candidate data from selection processes, an application was developed to migrate this data into a relational database. Detailed analysis was performed on the database-stored data, and various insightful chart visualizations were generated.



Key Concepts
------------

- **Data Ingestion:** The process of importing, transferring, loading, and processing data for later use or storage in a database.
- **Data Migration:** The process of moving data from one storage system or format to another, such as from a CSV file to a relational database.
- **Relational Database:** A type of database that stores data in tables with rows and columns, making it easier to organize and retrieve information using queries.
- **Data Visualization:** The graphical representation of data to help users understand complex data sets through visual elements like charts and graphs.

Technology Stack
----------------

- **Python:** A powerful programming language used for data handling and analysis.
- **Jupyter Notebook:** An open-source web application that allows you to create and share documents containing live code, equations, visualizations, and narrative text.
- **MySQL:** An open-source relational database management system that helps manage and organize data efficiently.

Steps Involved
--------------

1. **Data Ingestion:**
   
   - **Purpose:** To read and understand the structure of the CSV file containing candidate data.
   - **Process:** Use Python's pandas library to load the CSV file and perform initial data exploration.
   - For example,

     ..  code-block:: python
         
         import pandas as pd

         # Load the CSV file
         df = pd.read_csv('candidates.csv')

         # Display the first few rows
         print(df.head())
  

2. **Data Migration:**

   - **Purpose:** To move the data from the CSV file to a MySQL database.
   - **Process:** Establish a connection to the MySQL database using SQLAlchemy, create a table to store the candidate data, and insert the data into the database.
   - For example,

      ..  code-block:: python
         from sqlalchemy import create_engine

         # Create a connection to the MySQL database
         engine = create_engine('mysql+mysqlconnector://user:password@localhost/ws_001')

         # Write the data to the MySQL table
         df.to_sql(name='candidates', con=engine, if_exists='replace', index=False)
 

3. **Data Analysis:**

   - **Purpose:** To analyze the data stored in the MySQL database to derive meaningful insights.
   - **Process:** Query the MySQL database using SQLAlchemy and perform data analysis using pandas.
   - For example,

     ..  code-block:: python
         # Query the database
         query = 'SELECT * FROM candidates'
         df = pd.read_sql(query, engine)

         # Perform analysis (e.g., calculate average years of experience)
         avg_yoe = df['yoe'].mean()
         print(f'Average Years of Experience: {avg_yoe}')
     

4. **Data Visualization:**

   - **Process:** Query the MySQL database using SQLAlchemy and perform data analysis using pandas.
   - The visualizations expected are:
            - Hires by technology (pie chart)
            - Hires by year (horizontal bar chart)
            - Hires by seniority (bar chart)
            - Hires by country over years (USA, Brazil, Colombia, and Ecuador only)(multiline chart)    
   




Contents
--------

.. toggle:: Menu
   :animate: fade-in
   :color: primary

   .. toctree::
      :hidden:

      installation
      ingestion
      migration
      analysis
      visualization

