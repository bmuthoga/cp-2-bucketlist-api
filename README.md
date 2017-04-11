# cp-2-bucketlist-api [![CircleCI](https://circleci.com/gh/bmuthoga/cp-2-bucketlist-api/tree/tests.svg?style=svg)](https://circleci.com/gh/bmuthoga/cp-2-bucketlist-api/tree/tests) [![Coverage Status](https://coveralls.io/repos/github/bmuthoga/cp-2-bucketlist-api/badge.svg?branch=master)](https://coveralls.io/github/bmuthoga/cp-2-bucketlist-api?branch=master)
A Bucket List is a list of things that one has not done before but wants to do before dying. This is an API for an online Bucket List service using Flask-RESTful.

A user can create, update and delate bucket lists and items that belong to them. The API implements token-based authentication and stores its data in a sqlite database.


**Installation**

Clone this repo:

`git clone https://github.com/bmuthoga/cp-2-bucketlist-api.git`

Navigate into the app's directory:

`cd CP2-BUCKETLIST-API`

Create a vitual environment.

Install the required packages:

`pip install -r requirements.txt`

Create a .env file and set the following required environment variables in it:

| VARIABLE        | VALUE           | DESCRIPTION                        |
| --------------- |----------------:| ----------------------------------:|
| APP_SETTINGS    |                 | The workon environment.            |
| DATABASE_URL    |                 |   The URL to your database         |
| SECRET_KEY      |                 |    Set your preferred secret key   |


Create the database by running migrations:

`python manage.py db init`

`python manage.py db migrate`

`python manage.py db upgrade`

**Usage**

TO Run

`python manage.py runserver`

To test the API endpoints, use Postman.

**API Endpoints**

`POST api/v1/auth/login/`	Logs in a user	

`POST api/v1/auth/register/`	Register a new user	

`POST api/v1/bucketlists/`	Create a new bucket list	

`GET api/v1/bucketlists/`	List all created bucket lists	

`GET api/v1/bucketlists/?q=<query_string>`	Search for a bucket list by name

`GET api/v1/bucketlists/?limit=<limit>`	Paginates bucket list results	

`GET api/v1/bucketlists/<bucketlist_id>`	get single bucket list	

`PUT api/v1/bucketlists/<bucketlist_id>`	update single bucket list	

`DELETE api/v1/bucketlists/<bucketlist_id>`	Delete a single bucket list	

`POST api/v1/bucketlists/<bucketlist_id>/items/`	Create a new item in a bucket list	

`PUT api/v1/bucketlists/<bucketlist_id>/items/<item_id>`	Update an item in a bucket list	

`DELETE api/v1.0/bucketlists/<bucketlist_id>/items/<item_id>`	Delete an item in a bucket list

**TESTS**

To run tests

`nosetests --with-coverage`
