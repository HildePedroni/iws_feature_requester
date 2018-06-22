# Feature requester

[![Build Status](https://travis-ci.org/HildePedroni/iws_feature_requester.svg?branch=master)](https://travis-ci.org/HildePedroni/iws_feature_requester)

## About

A simple Flask application made to clients ho wants to have a better way to 
request new features for their softwares.

Whit this app, the client create a request that will be exposed for developer with a few steps.


<strong>The project lives at:</strong>

http://iws-feature-requester-dev.us-east-1.elasticbeanstalk.com/


## Developement

The app is being develped with Flask framework for backend and knockoutJS for front
    

### Set up environment

1 - clone the project
````console
    git clone https://github.com/HildePedroni/iws_feature_requester.git
````

2 - create a virtual env
    - Developed with python 3.6
    
````console
    python3 -m venv env 
````
3 - install requirements
````console
    pip install -r Requirements.txt 
````

4 - set up the database
    We use sqlite for developement
    Access python interactive shell at project root
````console
    python
    >>> from feature_requester import create_app
    >>> from feature_requester.models import db
    >>> db.create_all(app=create_app())
````    

5 - run tests

````console
    make tests 
````

### Deploy the application

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