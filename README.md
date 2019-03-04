# Movie REST API built with DRF

A basic movie database interacting with external API.


## Used technologies

<ul>
<li>Python</li>
<li>Django, Django Rest Framework (DRF)</li>
<li>PostgreSQL</li>
<li>django-filter</li>
<li>django-environ</li>
</ul>


## Installing

To install and run this project you must have to install locally PostgreSQL db service.

<ol>
<li>Install PostgresSQL service</li>
<li>Configure new database and db user, then fire up db service</li>
<li>Create .env file in email_api/email_api folder(right next to setting.py file), then fill it with your configuration:

```
# Django Settings
# ------------------------------------------
SECRET_KEY=
DEBUG=on


# PostgreSQL
# ------------------------------------------
POSTGRES_NAME=
POSTGRES_HOST=
POSTGRES_PORT=
POSTGRES_USER=
POSTGRES_PASSWORD=
```
</li>
<li>Create virtual environment and install requirements from requirements.txt file  
</li>
<li>Activate virtual environment 
</li>

<li>Fire up Django server:

```
python manage.py runserver
```
</li>
</ol>



### Testing app

Now you can open web broswer and hit url:  
http://localhost:8000/api/

Available api endpoints:  
  

| HTTP method              	| url       	        | available actions  	                        |
| -------------------------	| -------------------	| -----------------------------------------	    |
| POST, GET                 | api/movies      	    | add new movie, fetch list off all movies      |
| POST, GET               	| api/comments   	    | add new comment, fetch list off all comments  |
| GET	                    | api/top 	            | show top movies(based on number of comments) 	|

