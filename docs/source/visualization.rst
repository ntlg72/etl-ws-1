Visualization
-------------

The process conducted in this section involves the connection of the database to a visualization tool to obtain 4 charts:

- Hires by technology (pie chart)
- Hires by year (horizontal bar chart)
- Hires by seniority (bar chart)
- Hires by country over years (USA, Brazil, Colombia, and Ecuador only)(multiline chart)

Firt, we have to login into Redash as explained in the project´s README.

.. contents::
   :local:



Connect to a Data Source
""""""""""""""""""""""""
 

Before you we can write queries, we need to connect Redash to a data source. We navigate to the 'Settings' and add our data source (select "PostgreSQL") with the appropriate credential, and the WSL 2 instance IP as host

   .. image:: ../images/redash_pg.png
      :align: center
      :width: 500px 


Create queries
""""""""""""""

Redash comes with an interface to write and run queries on the platform.

Just click on the “New Query” button, type a name for your query (otherwise, it will be considered a draft), copy and paste the query inside the text area, and click on the “save” button.

   .. image:: ../images/queries.png
      :align: center
      :width: 500px 


Create visualizations for the query
"""""""""""""""""""""""""""""""""""

All saved queries by default have a ‘Table’ visualization created. We can create more visualizations after the query runs for the first time.

The options are:

- Chart
- Cohort
- Counter
- Map
- And more.

Click on the “+ Add Visualization” button, select the visualization type, set a name and options for the visualization, and then click “save” and "publish".

   .. image:: ../images/visualization.png
      :align: center
      :width: 500px 


Create a dashboard
""""""""""""""""""
A dashboard is composed of widgets, which can be any visualization created from the query source page. The dashboard is created by clicking on the “New Dashboard” button on the homepage, assigning it a name, and then clicking on the “save” button.

You can also, at any time, create a dashboard by clicking on the dropdown menu on the fixed navbar.

After this, you will have an empty page with the dashboard name.  Click the 3 dots button on the top right and choose "Edit". 


    .. image:: ../images/dashboard1.png
          :align: center
          :width: 600px 
    


Then click on the "Add Widget", select your query and its visualization.


    .. image:: ../images/widget.png
          :align: center
          :width: 600px 


    .. image:: ../images/add_widget.png
          :align: center
          :width: 600px 


Dashboard results
"""""""""""""""""
    .. image:: ../images/dashboard.png
          :align: center
          :width: 600px 


   

.. note::

    - One of the requested visualizations was “Hires by Country Over Years” for Brazil, Colombia Ecuador and the United States. However in the visualization there are 5 lines. This is due to the coding done by ``pycountry``, which recognizes and labels some countries as overseas territories of the United States (the United States Minor Outlying Islands line).

    - In the pie chart, technologies with less than 250 hirees are grouped into the category of "Others" for better visualization.
    

Conclusions
""""""""""""

1. The hiring percentages in different technology areas indicate that certain specialties, such as DevOps (12.5%) and System Administration (28.7%), are in significantly higher demand compared to other areas.This is interesting given the high count of candidates applying for these areas. The hiring percentages in DevOps and System Administration reflect their critical role in IT ecosystems, but the high applicant count suggests stiff competition and potential skill mismatches


2. The slightly higher number of hires for interns and trainees suggests that the organization could be investing in future talent, potentially focusing on developing employees from early career stages. This approach can be cost-effective and beneficial for building a strong organizational culture, as junior hires often bring fresh perspectives and innovation. Additionally, it may indicate a strategy to address high turnover in junior roles or support company growth by filling new positions with entry-level talent.  Also Interns and trainees tend to have lower salaries compared to more senior professionals, which can be attractive to the organization in terms of costs.

    At the same time, the balanced hiring across seniority levels shows that the organization is also valuing experienced professionals, ensuring stability and leadership. This equilibrium reflects a healthy organizational structure, where junior employees are supported by senior mentors, fostering a culture of learning and growth. Overall, the hiring pattern suggests a sustainable strategy that balances immediate needs with long-term talent development.


3. Hiring numbers remained consistently high from 2018 to 2021, with a slight increase observed between 2018 and 2019. The apparent decrease in 2022 may be attributed to the limited data scope, as the dataset only includes information up to July 2022, rather than reflecting a full-year trend. This analysis highlights the dynamic nature of hiring patterns in response to external factors and underscores the importance of considering data limitations when interpreting trends.


4. The hiring trends by Country Over Year reflect a clear response to external factors which drove a significant demand for technology roles in 2020. The subsequent decline may be linked to market saturation, economic stabilization, and momst importantly to *limitations of the dataset*, which only covers the first half of 2022. 


    Hiring in Colombia remained stable through 2020, but fell sharply after 2021. This decline may be related to specific factors such as changes in the labor market or the impact of external events.

    United States and Brazil: Although both countries show a decline towards the end of the period, the United States shows a small peak in 2020, while Brazil maintains more intermediate fluctuations.

    Ecuador Shows Variability: Ecuador exhibits a pattern of ups and downs, highlighting its increase in 2019 and 2021, but ending with a decline in 2022.

    U.S. Minor Outlying Islands: Although they start with the highest number of hires, they also show a steady decline by 2022.