Instructions to use this DB.

Requirements:
- Create a database called "codewars"

Instructions:
- Run the following commands:
    $ flask db init ## This creates the migrations directory
    $ flask db migrate ## This creates the migration scripts
    $ flask db upgrade ## This runs the migrations scripts
- Run "$ flask run" to start the flask app and make the first call to codewars to update the db.