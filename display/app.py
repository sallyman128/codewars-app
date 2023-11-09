# consumer/app.py

### Display the raw data and the analytic data


from flask import Flask
from celery import Celery
import pika

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'pyamqp://guest:guest@rabbitmq:5672//'
app.config['CELERY_RESULT_BACKEND'] = 'rpc://'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='example-queue')

messages = []

@celery.task
def process_message():
    method_frame, header_frame, body = channel.basic_get(queue='example-queue')
    messages.append(body)
    if method_frame:
        print(f"Processing message: {messages}")
        # Add your processing logic here
    else:
        print("No messages in the queue.")

@app.route('/')
def consume_message():
    # Trigger the Celery task to process the message asynchronously
    process_message.apply_async()
    return '[]'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
