from flask import Flask
from models import db
from flask_migrate import Migrate
from fetch_data import add_daily_data_from_codewars
from sqlalchemy import inspect


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///codewars'

db.init_app(app)
migrate = Migrate(app, db)

def does_table_exist():
    inspector = inspect(db.engine)
    return inspector.has_table("language")

with app.app_context():
    # Fetch daily data from API
    if does_table_exist(): add_daily_data_from_codewars()