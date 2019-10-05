# weathered_back

This is the backend of a weather web application. You can find the frontend [here](https://github.com/romain-ngo/weathered_front).

## Launch app

1. Create a `.env` file in the root folder and set the following variables: 

```.env
TESTING=True | False 
FLASK_DEBUG=True | False (print error message)
SECRET_KEY=string
DB_DIALECT=sqlite | postgresql | mysql | many more
DB_FILE=name_of_the_database_file
DB_TRACK_MODIFICATIONS=True | False
```
**/!\\ Add `.env` to `.gitignore` and make sure it is never committed /!\\**

2. You can start the flask application by starting the bash script `start.sh` located in the root folder by running:

```bash
sh start.sh
```

You can also run the application manually with the following commands:

```bash
export FLASK_APP = app.py
export FLASK_ENV=development
flask run
```

## Application factory

The structure of this flask application is based on the application factory.  
The entry point of the application is `wsgi.py`. This file will call the __init__.py located in the `application/` folder.  
The application make use of blueprints in order to separate each sub application into their own module.

## Database
We make use of flask-sqlalchemy in order to connect to a database. Flask-sqlalchemy is an ORM (Object Relationnal Mapper) having the ability to change dialects easily.
In a production environment, we use SQLite but make sure to use a more suited RDBMS such as PostgreSQL.
The configuration is done in `config.py` but the valued are set in `.env`

1. Create the model
2. Create the migration repository: `flask db init`
3. Create the database migration: `flask db migrate`.  
This will create a script with the modifications that has to be made to the database only if there are any.
4. Apply the changes to the database by running: `flask db upgrade`.  
If you are using sqlite, if the database file does not exist, this command will create it.

### Updating the database
If the database structure needs to be modified, make the change in the model locally, then generate a new migration file.  
Apply the modifications with `flask db upgrade`. If any mistakes are made and we need to revert back to a previous structure, use `flask db downgrade`.

## API 

### User

* Add new user  
`POST /user`
```json
{
  "email": "",
  "username": "",
  "password": ""
}
```

* Edit a user  
`PUT /user/:id`
```json
{
  "email": "",
  "username": "",
  "password": ""
}
```

* Log in  
`GET /login`
```json
{
  "email": "",
  "password": ""
}
```

* Log out  
`POST /logout`
```json
{
  "email": ""
}
```

* Get locations of user 
`GET /user/:id/locations`

### Location

* Add new location
`POST /location`
```json
{
  "id": 0,
  "country": "",
  "city": "",
  "latitude": 0,
  "longitude": 0
}
```