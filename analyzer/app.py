from flask import Flask, request, abort
from models.analytics import Analytics
import requests
import json
from flask_cors import CORS
from celery import Celery

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# RabbitMQ configuration
RABBITMQ_BROKER = 'pyamqp://guest:guest@rabbitmq:5672//'
RABBITMQ_QUEUE = 'events'

# Celery configuration
celery = Celery(__name__, broker=RABBITMQ_BROKER)

@celery.task
def publishEvent(event):
    with celery.connection_or_acquire() as conn:
        with conn.SimpleQueue(RABBITMQ_QUEUE) as queue:
            queue.put(event)

@app.route('/')
def hello_world():
    return 'Hello, Analyzer!'

@app.route('/fetchcodewars')
def fetchCodewars():
    event_request_received = {"eventType": "REQUEST_RECEIVED", "payload": None}
    publishEvent.apply_async(args=[event_request_received])

    username = request.args.get('username')
    api_data = fetch_data_from_codewars(username)

    if api_data:
        name = api_data['name']
        leaderboardPosition = api_data['leaderboardPosition']
        language_scores = {language: details["score"] for language, details in api_data['ranks']['languages'].items()}
        topLanguage = max(language_scores, key=lambda lang: language_scores[lang])

        analytics = Analytics(name, leaderboardPosition, language_scores, topLanguage)
        json_analytics = json.dumps(analytics.to_dict())

        event_response_sent = {"eventType": "RESPONSE_SENT", "payload": json_analytics}
        publishEvent.apply_async(args=[event_response_sent])

        return json_analytics
    else:
        event_invalid_username = {"eventType": "INVALID_USERNAME", "payload": None}
        publishEvent.apply_async(args=[event_invalid_username])
        return abort(400, "Invalid username")

def fetch_data_from_codewars(username):
    api_url = f'https://www.codewars.com/api/v1/users/{username}'
    response = requests.get(api_url)

    if response.status_code == 200:
        return response.json()
    else:
        print("Error: No response from codewars")
        return None