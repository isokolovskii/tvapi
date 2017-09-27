# TV Restful API
This application is a part of TV project group aimed to 
deliver great experience in browsing TV schedule.

This is REST API which main goal is to give mobile, web, 
desktop and other applications to get all data about schedule.

Application is based on Flask-restful, uses SqlAlchemy for 
communications with MySQL database. 

##Contents:
#### config.py
API server configuration. It consists of config 
dictionary with database management system info(***mysql***),
database driver info(***pymysql***), database user and 
password, database server location and database scheme. Also
provides info about database charset and host:port for API
server to start.
Last thing is database URI for SqlAlchemy connection.


#### database.py
Creates session for communication with database with bind
engine created for database URI from configuration.
After session initialization creates scoped session for use
in application.

#### models
Models module.
Classes bind tables from database.

#### resources
Resources module for use in Flask API.
Classes use model and scoped session from ***database.py***
to execute queries on database and return results as JSON 
objects.

#### tvrestapi.py
Main application script.
Creates Flask app and instantiates Flask API for this app,
then add resources to that API from resources module and
binds it to API routes. 
Then runs API server.

#### api_test.http
File contents test API requests for application testing.