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

2 - create a virtual env

3 - install requirements

4 - set up the database

5 - run tests



4 - In python interactive shell
````console
>>> from feature_requester import create_app
>>> from feature_requester.models import db
>>> db.create_all(app=create_app())
````


<strong>Under contruction</strong>

The next steps will be added later 


### Deploy the application

The application is deployed with AWS elastic beanstalk cli.

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