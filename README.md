##Process to run the project##
===============================================
for Windows system
----------------------------
1) check Python Version if its available then its good otherwise install python
2) open project
3) run this command **py -3 -m venv venv**
4) run this command **venv\Scripts\activate**
5) run this command **cd .\weather_api_service\**
6) run this command **pip install -r requirements.txt**
7) run this command set FLASK_APP=__init__.py
8) run this command $env:FLASK_APP = "__init__.py"
9) run this command flask run

login api call
------------------------
request type -> POST
url -> http://127.0.0.1:5000/login
body -> {
    "user_name":{user_name},
    "password":{password}
}


country Api call
--------------------------
rest type -> GET
url -> http://127.0.0.1:5000/countries
authorization -> bearer token

example => http://127.0.0.1:5000/countries

city Api call
--------------------------
rest type -> GET
url -> http://127.0.0.1:5000/cities?country={county_name}
authorization -> bearer token

example ->http://127.0.0.1:5000/cities?country=Andorra

forecast Api call
--------------------------
rest type -> GET
url -> http://127.0.0.1:5000/forecast?q={country_name}&no=no&days={days}
authorization -> bearer token

example -> http://127.0.0.1:5000/forecast?q=Canada&no=no&days=2

city Api call
--------------------------
rest type -> GET
url -> http://127.0.0.1:5000/analytics?filter={filter_condition}&top={upcomming_days}
authorization -> bearer token

example => http://127.0.0.1:5000/analytics?filter=country&top=2
