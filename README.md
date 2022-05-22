# Air-Quality-in-the-Cloud
School Project: Generate an application to be a dashboard that displays specific air quality data in Los Angeles (in Chile, not the U.S.) using the Open AQ API. 

Provided with the openaq.py file to help communicate with the Open AQ API, I built a Flask-powered web application that displays data about air quality. I pulled 100 observations of measurements of fine particulate matter (PM 2.5) in the Los Angeles area by incorporating specific requests into my application as a function called get_results: 
- Imported and set up the API object in my aq_dashboard.py file
- Retrieved the data from the API when the main ('root') route is called
- Created a list of (utc_datetime, value) tuples
- Returned this list in the main route, so that the home page of the web application displays the raw list of tuples
In order store this extracted information into a database, I created a Record model with attibutes "ID", "datetime", and "value" using flask_sqlalchemy.

Then revisiting the main route, the database was filtered for any Record objects that have value greater than or equal to 18. Finally, I returned this filtered list of "potentially risky" PM 2.5 datetime/value tuples (converting to string for Flask). The result is a basic dashboard that stores, updates, and displays useful data about the air quality in Los Angeles area. 
