# P3_Nobel_Pyze

**Team #3 Members:**

Project Contributors:
- Steven Bonillas (/S-Bonillas)
- Sequoia Boubion-Mckay (/Sequoiabm)
- Garima Chaudhary (/garimac12)
- Angel Alcala Ruiz (/dejesusalcala)
- Rania Shaker (/rshaker101)

**Video Link:**
- https://drive.google.com/file/d/1TPZwo8BAa0A5I4jWmthOhkOnwOigVcIR/view?usp=drive_link

**Project Abstract and Overview:**
- Utilizing nearly a thousand records, direct from the Nobel Prize Committee, this projects seeks to visualize and contextualize the data that the committe keeps on their laureates.  Analyizing location, gender, and age data, the Nobel_Pyze project has created multiple interactive visualizations to help users explore this extraordinary dataset.

- The project dataset was pulled from the Nobel Prize API (https://nobelprize.readme.io/reference/getting-started).  The data was pulled via Python in Jupyter Notebook, then sorted and cleaned using Pandas. 

- The cleaned data was then exported from Jupyter Notebook into the CSVs which made up our SQL tables.  The team developed a  SQL Schema which accepted and sorted the CSVs into a cohesive database. An ERD of the database structure (Nobel_Pyze_ERD.png) as well as a saved copy of our schema (./resources/Nobel_Pyze_Schema.sql) are available in this repository.

- The project team then designed a Flask/SqlAlchemy applet which connected our systems directly to the database.  For some visualizations, the static data was extracted from the SQL server as a JSON file (.resources/AllTables.json).  

- The Data Visualizations are presented on a custom dashboard, which displays a data and factoids section that is also fueled by JavaScript.  There are three separate, interactive visualizations on the page.  At the bottom is a link to our interactive map. 

- Our Fact table shows totals of the prize monies awarded, the university with the most Laureates honored, and the top three countries where Laureates were born.  We also show a count of total laureates, separate them by gender, and determine if the prize was awarded to an organization or not.

- Our first interactive chart displays the distribution of laureates by age. Values for both male and female laureates is visible throughout.  The chart allows users to view the data as a whole, or by category.

- The second visualization shows the distribution of laureates by gender.  Users can choose to view the data as a stacked bar or stacked line chart. We can see that the vast majority of laureates are male. When comparing this to the first visualization, we can see that the gender distribution tends to even (slightly) for the Peace and Literature categories.  Our current theory is that this is indicative of historically low representation in STEM subjects. This is deserving of further research and would benefit from comparing Laureate data with nominee data.

- Winners of the Nobel Prize often share the award with others, as they often work within teams.  The third visualization allows users to see the number of Solo Laureates compared to the number of Shared Laureates.  The dropdown options switch between displaying all of the data in the set, or Sole Winners vs Shared Winners, or showing a drill-down distribution of how the prizes are shared, either between two people, three people, or four.  The largest group of shared laureates in our data was four.

- The interactive map displays the birthplaces of Nobel Laureates across the globe.  The map features custom, clustering markers, that auto-bloom and shrink when zooming in and out. When a marker is clicked, the user is shown the Laureate's name, birthplace, their category, the reason for their award, and the date they received it. The markers also have external links, which if the user clicks on them, they will be taken to a small write-up on the Laureate for more information. 

- The map has filters in place to allow users to filter the types of Laureates they want to view by both their winning category and by the date when their prize was awarded.  The filters work in conjunction, and will allow for filtering by type and time concurrently. For different visual preferences, the map is also capable of changing between the Default View, a Dark Mode, and a Light Mode.  The data is visible in all three versions.  The map is fed by a Real-Time API pull from the SQL server, but if that fails, the map has a failsafe to pull from the local backup in the resources folder.

**Sources and Methods:**
- The Nobel Prize Committee (http://www.nobelprize.org)
- The Nobel Prize API (https://nobelprize.readme.io/reference/getting-started)
- Open Street Maps (http://www.openstreetmap.org)
- Leaflet (https://leafletjs.com/plugins.html)
- plotly (https://plotly.com/)
- SQLAlchemy (https://www.sqlalchemy.org/)
- Flask (https://flask.palletsprojects.com/en/3.0.x/)

**Project files:**

**'P3_Nobel_Pyze' Folder contains:**
- index.html (HTML which contains the dashboard, visualizations, and link to the interactive map)
- heatmaps.html (HTML for the interactive map)
- Nobel_Pyze_ERD.png (Map of the SQL Schema - the actual schema is in the resources folder)
- P3_Nobel_Pyze.ipynb (Jupyter Notebook, containing Python code, which calls the Nobel API, then parses, cleans, and exports the data)
- FlaskAPI.py (Python program which uses Flask and SQLAlchemy to connect our systems to the SQL server and generates an API which our team called on to feed our data into our final product)
- .gitignore (Holds back the version of FlaskAPI.py which contains SQL login information)
- Nobel_Pyze_Presentation.pdf (PDF copy of the slide Deck for the video presentation)
- LICENSE (MIT license)
- README.md (The file which you are reading right now)


**'P3_Nobel_Pyze > Resources' Folder contains:**
- AllTables.JSON (JSON file exported from the SQL API, created after the Flask connection)
- Laureate_Data.json (Raw pull from Nobel API, data to be cleaned, saved so as not to have to poll the API again)
- Laureates.csv (CSV exported from a Python dataframe, used for later cleaning)
- LaureatesAndAwards.js (DataSet derived from AllTables.JSON, used in DataVisualization 2)
- Nobel_merged.csv (Midpoint in cleaning, combining separate dataframes together, saved to prevent re-work)
- Nobel_prizeWinners.json (Raw pull from Nobel API, data to be cleaned, saved so as not to have to poll the API again)
- Nobel_Pyze_Schema.sql (SQL Query, which created the tables for our database. Exported from pgAdmin)
- Orgs.csv (Splintered dataset, needed to be cleaned before being reintroduced to the main body, contains data on organizational winners)
- sql_awards.csv (Cleaned data, ready for upload to the SQL 'Awards' table)
- sql_laureates.csv (Cleaned data, ready for upload to the SQL 'Laureates' table)
- sql_orgs.csv (Cleaned data, ready for upload to the SQL 'Orgs' table)
- sql_prizes.csv (Cleaned data, ready for upload to the SQL 'Prizes' table)
- test.ipynb (Jupyter notebook, used for pip-installs to get the SQL Alchemy working in VS Code)
- Winners.csv (Midpoint in cleaning, combining separate dataframes together, saved to prevent re-work)

**'P3_Nobel_Pyze > static > css' Folder contains:**
- map.css (Style document for the Interactive Map - heatmaps.html)
- style.css (Style document for the Dashboard - index.html)

**'P3_Nobel_Pyze > static > img' Folder contains:**
- map_pic.png (Screenshot of the Interactive Map to be used as a hyperlink on index.html that directs to heatmaps.html)

**'P3_Nobel_Pyze > static > js' Folder contains:**
- app-AR.js (JavaScript for visualization 1 on the dashboard)
- GCplots1.js (JavaScript for Visualization 2 on the Dashboard)
- heatmap.js (JavaScript for the Interactive Map)
- logic.js (JavaScript for the Dashboard on index.html)
- nobeldata.js (JavaScript, but technically a JSON, used as a datasource for Visualization 1, derived from AllTables.json)
- sole.js (JavaScript for Visualization 3 on the Dashboard)

**'P3_Nobel_Pyze > working' Folder contains:**
- GCindex1.html (Preliminary visualization for Visualization 2, created prior to being added to the dashboard)
- index-AR.html (Preliminary visualization for Visualization 1, created prior to being added to the dashboard)