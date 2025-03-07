Transformation & Load
---------------------



.. contents::
   :local:



The process conducted in this section involves the application of a series of transformations on the‘candidates’ data migrated to the PostgreSQL database.Here, the data is transformed and consolidated for its intended analytical use case. Then the transformed data is moved into a target data database. This section is linked to the ``001_tl.ipynb`` notebook of the project.


Importing libraries
"""""""""""""""""""

import os
import sys
import numpy as np 
import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns
from fuzzywuzzy import process
import pycountry
sys.path.append(os.path.abspath('../src'))
from connection.db_utils import get_connection, close_connection


Establishing the database connection
""""""""""""""""""""""""""""""""""""

Database connection is done in the same way as in the extraction and EDA process.


Reading the candidates data from the PosgreSQL database
"""""""""""""""""""""""""""""""""""""""""""""""""""""""

This process is done in the same way as in the EDA process.


Column names
^^^^^^^^^^^^^

Database table names, column names, index names, etc. should follow a naming convention that ensures high readability and uses the English language (in general). In this case the columns follow the guidelines, but can be formated to be in lowercase letters, and their spaces replaced by underscores.

The first line of code, focuses on standardizing column names by replacing spaces with underscores. This is achieved by accessing the column names through ``df.columns``, using the ``.str`` accessor to apply string operations element-wise, and then utilizing the ``.replace(' ', '_')`` method to perform the substitution. The modified column names are then reassigned back to ``df.columns``.

Following this, the second line further cleans the column names by converting all characters to lowercase. The ``df.rename()`` method is employed with the `columns=str.lower` argument, which applies the `str.lower` function to each column name. The result is a new DataFrame with all column names in lowercase


.. image:: ../images/snake_case.png
   :align: center
   :width: 600px 

.. note::

    Now all columns are in *Snake case* , a way of writing phrases without spaces, where spaces are replaced with     
    underscores, and the words are typically all lower case. 


Obtaining the hired candidates
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A candidate is considered HIRED when she/he has both scores greater than or equal to 7.

This code defines a function mark_hired_candidates that processes a DataFrame (df) containing candidate data. It creates a new column called hired in the DataFrame. The value in this column is determined by a logical condition: a candidate is marked as True (hired) if their code_challenge_score is greater than or equal to 7 and their technical_interview_score is also greater than or equal to 7. Otherwise, the value is False. Finally, the modified DataFrame is returned. By calling mark_hired_candidates(df), the function applies this logic to the DataFrame and updates it to include the hired column, which indicates whether each candidate meets the hiring criteria.
