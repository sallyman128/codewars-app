from flask_sqlalchemy import SQLAlchemy
from datetime import date

db = SQLAlchemy()

class Language(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    language = db.Column(db.String)
    color = db.Column(db.String)
    score = db.Column(db.Integer)
    date = db.Column(db.Date, default=date.today())