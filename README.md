# Feature requester

[![Build Status](https://travis-ci.org/HildePedroni/iws_feature_requester.svg?branch=master)](https://travis-ci.org/HildePedroni/iws_feature_requester)

## About

A simple Flask application made to clients ho wants to have a better way to 
request new features for their software.

Whit this app, the client create a request that will be exposed for developers who will implement them.

<strong>The project can be viwed live at:</strong>

<strong>The app is not live anymore:</strong>



## App stage
This project is a minimum viable product (MVP) based on given requirements.
A lot of features can be implemented to make it a complete product. 
Features like filtering by clients, creating new clients and so on.
The UX can be improved too, things like card color changing when due date approaches 
and better error ans success feedbacks.



## Technologies used
#### For developement
- Backend

    Python 3.6, Flask, SqliteAlchemy, Sqlite

- Frontend 
    Bootstrap 4, KnockoutJS, Jquery

#### For deployment
- AWS Elastic Beanstalk.
- Deploy with eb CLI
- Database Mysql


## To run the project on a local machine
    
### Set up environment

##### 1 - clone the project
````console
    git clone https://github.com/HildePedroni/iws_feature_requester.git
````

##### 2 - create a virtual env
    
````console
    python3 -m venv env
````
- Activate the virtual environment

```console
    source env/bin/activate
```

##### 3 - install requirements
````console
    pip install -r Requirements.txt 
````

##### 4 - Create a .env file on project root and add the following variables:
````dotenv
DEBUG=True

DB_HOSTNAME=localhost
DB_USERNAME=root
DB_PASSWORD=root
DB_NAME=ebdb

AWS_ACCESS_KEY_ID=Your_key_id_or_leave_blank
AWS_SECRET_ACCESS_KEY=your_access_key_or_leave_blak
````    
The above variables are required, but with except DEBUG they all can be left blank        
If you set DEBUG to false, you will have to set-up a MySQL database, or change the config.py file to use whatever database you like

##### 5 - set up the database
For development SQLite was used. 
To create the database access the python interactive shell at the project root
````console
    python
    >>> from feature_requester import create_app
    >>> from feature_requester.models import db
    >>> db.create_all(app=create_app())
````    

##### 6 - run tests

````console
    make test
````

##### 7 - To run the application locally, run
````console
    python application.py
````

## To Deploy the application

The application is deployed with AWS elastic beanstalk cli. 
With a mysql database

To install fallow the instructions at:

https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install.html

To configure fallow the instructions at:

https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-configuration.html

You have to have the aws credentials to config the environment

After configuration done, use 

```console
    eb deploy
```` 
to deploy the application

Hope you enjoy
