Data Migration
================


.. contents::
   :local:


In general, data migration means moving digital information. Transferring that information to a different location, file format, environment, storage system, database, datacenter, or application all fit within the definition of data migration. In this case, we migrate de *candidates.csv* Pandas DataFrame into a MySQL table.


MySQL Table Design 
------------------


1. Naming Conventions
^^^^^^^^^^^^^^^^^^^^^

Database table names, column names, index names, etc. should follow a naming convention that ensures high readability and uses the English language (in general). When someone looks at the name, they should be able to understand its meaning.

.. caution::

   Table names and column names should be in lowercase letters or numbers. 

To standarized columns, the ``clean_column_names(df)`` is used in the *001_e.ipynb* notebook. This function cleans and standardizes column names in a Pandas DataFrame to conform to database naming conventions.It performs the following transformations:

    - Replaces spaces in column names with underscores.
    - Converts column names to lowercase.

It takes as input the DataFrame whose column names will be cleaned, and returns the modified DataFrame with cleaned column names.
                         

2. Choosing Appropriate Field Types
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When designing tables, it is important to choose appropriate and efficient field types. 

.. note::

   Data profiling informs and validates the MySQL table design: it determines appropriate data types and lengths based on 
   actual data values.

   For example, if profiling reveals that the longest email is 36 characters, you might set the email column to 
   VARCHAR(50) to provide a margin.


The information obtained during the data profiling process (see :ref:`Profiling data types`) contributes to choosing appropriate data types for the MySQL table design by showing the correspondence between the Pandas data types and suggested MySQL data types. 

.. code-block:: shell


    Column 'First Name': Pandas dtype = object, Suggested MySQL type = VARCHAR(11)

    Column 'Last Name': Pandas dtype = object, Suggested MySQL type = VARCHAR(13)

    Column 'Email': Pandas dtype = object, Suggested MySQL type = VARCHAR(36)

    Column 'Application Date': Pandas dtype = object, Suggested MySQL type = VARCHAR(10)

    Column 'Country': Pandas dtype = object, Suggested MySQL type = VARCHAR(51)

    Column 'YOE': Pandas dtype = int64, Suggested MySQL type = <class 'sqlalchemy.sql.sqltypes.SmallInteger'>

    Column 'Seniority': Pandas dtype = object, Suggested MySQL type = VARCHAR(9)

    Column 'Technology': Pandas dtype = object, Suggested MySQL type = VARCHAR(39)

    Column 'Code Challenge Score': Pandas dtype = int64, Suggested MySQL type = <class 'sqlalchemy.sql.sqltypes.SmallInteger'>

    Column 'Technical Interview Score': Pandas dtype = int64, Suggested MySQL type = <class 'sqlalchemy.sql.sqltypes.SmallInteger'>.
    

.. attention::

  "Application Date" should ideally be changeg to MySQL's DATE, DATETIME, or TIMESTAMP type. And shorter VARCHAR lengths    
  and smaller integer types are to be considered if one is sure the range is sufficient.



3. Choosing Appropriate Field Length
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When designing tables, it is necessary to consider field lengths. 


VARCHAR lenghts
"""""""""""""""

The suggested maximum VARCHAR lengths for the columns are based on the maximum observed values during the data profiling process( see :ref:`Profiling the lenght of string values`) , plus some margin for safety. Here are the chosen data types considering the maximum string lengths to improve performance and storage.:

- **First Name:** VARCHAR(20) to handle names up to 11 characters with some extra space.
- **Last Name:** VARCHAR(20) for names up to 13 characters with some additional margin.
- **Email:** VARCHAR(50) to handle emails up to 36 characters plus some buffer.
- **Application Date:** VARCHAR(60)  to dates up to 10 characters with some extra space. It will be transformed in the future.
- **Country:** VARCHAR(60) for country names up to 51 characters.
- **YOE:** TINYINT UNSIGNED, suitable for storing small integer values (0-255).
- **Seniority:** VARCHAR(15) for values up to 9 characters plus margin.
- **Technology:** VARCHAR(50) to handle up to 39 characters plus some buffer.
- **Code Challenge Score:** TINYINT UNSIGNED to store small integer scores (0-255).
- **Technical Interview Score:** TINYINT UNSIGNED to store small integer scores (0-255).


Creation
^^^^^^^^

Using a a Class to create the table
"""""""""""""""""""""""""""""""""""

Using a class to define the table structure leverages Object-Relational Mapping (ORM). ORMs map class definitions in code to relational database tables, providing several benefits:

- **Abstraction and Convenience:** By using classes, you interact with the database through objects and methods instead of writing SQL queries directly. This abstracts the database interaction, making code easier to write, read, and maintain.

- **Type Safety:** ORM enforces type safety. This means you define the data types once in your class, and the ORM ensures that the database and your code adhere to these types, reducing the risk of runtime errors.
    
- **Maintainability:** Changes to the database schema are easier to manage. If you need to add, modify, or remove a column, you update the class definition, and the ORM handles the database changes.
    
- **Reusability:** The class can be reused in different parts of the application.
    
- **Consistency:** Using classes ensures consistent handling of database operations across the application. The table structure is defined once, and the ORM uses this definition for all interactions.

Implementation
""""""""""""""

The process begins with defining a function, ``get_engine()``, which establishes a connection to a MySQL database using SQLAlchemy. This function retrieves database credentials (username, password, host, port, and database name) from environment variables and constructs a connection string.  It then uses this string to create a SQLAlchemy engine, which manages the communication with the database.  

Once the table structure is defined in the Applicants class, the create_tables() function is responsible for actually creating the table in the MySQL database.  This function uses the engine created by ``get_engine()`○ and the metadata associated with the Base class to issue the necessary SQL commands to create the table.  The if __name__ == "__main__": block ensures that the create_tables() function is called only when the script is executed directly (not when it's imported as a module).  This block effectively starts the process of establishing the database connection, defining the table schema, and creating the table in the MySQL database if it doesn't already exist. The process effectively leverages SQLAlchemy's ORM capabilities to map Python classes to database tables and automate the creation process.


3. class Applicants(Base)
**************************

Next, a base class (``Base``) is created using ``declarative_base()``. This base class serves as a container for table metadata and is used to define table structures in a declarative way.  The ``Applicants`` class inherits from this base and defines the structure of the "candidates" table.  Within this class, each attribute represents a column in the table, specifying the column name, data type (e.g., String, Integer, SmallInteger), and constraints (e.g., nullable=False).


.. image:: ../images/table-create.png
   :align: center
   :width: 600px 

.. tip::

   To verify the table attibutes, after switching to the *ws_001* databases, the command is ``DESC candidates`` used.

   .. image:: ../images/candidates-desc.png
     :align: center
     :width: 600px 


3. Choosing Appropriate Field Length
************************************

Once the table structure is defined in the ``Applicants`` class, the ``create_tables()`` function is responsible for actually creating the table in the MySQL database.  This function uses the engine created by ``get_engine()`` and the metadata associated with the ``Base`` class to issue the necessary SQL commands to create the table.  The ``if __name__ == "__main__":`` block ensures that the create_tables() function is called only when the script is executed directly (not when it's imported as a module).  This block effectively starts the process of establishing the database connection, defining the table schema, and creating the table in the MySQL database if it doesn't already exist. The process effectively leverages SQLAlchemy's ORM capabilities to map Python classes to database tables and automate the creation process.


.. image:: ../images/data-insert.png
   :align: center
   :width: 600px


.. tip::

   To verify the table registers, after switching to the *ws_001* databases, the command is ``SELECT COUNT(id) FROM candidates`` used. It should show the 50.000 number, according to the number of columns that running ``df`` showed during the data ingestion process.


.. image:: ../images/rows.png
   :align: center
   :width: 600px
