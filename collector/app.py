from flask import Flask
from models import db
from flask_migrate import Migrate
from fetch_data import add_daily_data_from_codewars
from sqlalchemy import inspect, create_engine
from sqlalchemy_utils import database_exists, create_database
import os

engine = create_engine(os.environ.get('DATABASE_URL'))
if not database_exists(engine.url):
    create_database(engine.url)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

db.init_app(app)
migrate = Migrate(app, db)

def does_table_exist():
    inspector = inspect(db.engine)
    return inspector.has_table("language")

with app.app_context():
    # Fetch daily data from API
    if does_table_exist(): add_daily_data_from_codewars()

## NOTE just for testing the service... delete in the end...
@app.route("/") 
def index(): 
    return "Collector is working"