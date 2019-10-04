# weathered_back

This is the backend of a weather web application.

## Launch app

```
export FLASK_APP = app.py
export FLASK_ENV=development
flask run
```

## Database
1. Create the modell
2. Create the migration repository: `flask db init`
3. Create the database migration: `flask db migrate`.  
This will create a script with the modifications that has to be made to the database only if there are any.
4. Apply the changes to the database by running: `flask db upgrade`.  
If you are using sqlite, if the database file does not exist, this command will create it.

### Updating the database
If the database structure needs to be modified, make the change in the model locally, then generate a new migration file.  
Apply the modifications with `flask db upgrade`. If any mistakes are made and we need to revert back to a previous structure, use `flask db downgrade`.