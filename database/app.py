from celery import Celery
from sqlalchemy import create_engine, Column, Integer, String, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json

# RabbitMQ configuration
RABBITMQ_BROKER = 'pyamqp://guest:guest@rabbitmq:5672//'
RABBITMQ_QUEUE = 'events'

# SQLAlchemy configuration
DB_URL = 'postgresql://usr:pswd@postgres:5432/codewars_db'

Base = declarative_base()

class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    eventType = Column(String(255))
    payload = Column(String(255))

# Create the database engine
engine = create_engine(DB_URL)

# Create tables
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Celery configuration
celery = Celery(__name__, broker=RABBITMQ_BROKER)

@celery.task
def save_to_database(event):
    event_instance = Event(eventType=event['eventType'], payload=event['payload'])

    # Add the event to the session
    session.add(event_instance)
    
    # Commit the transaction
    session.commit()

if __name__ == '__main__':
    celery.worker_main()
