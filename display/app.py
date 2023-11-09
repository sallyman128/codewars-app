# consumer/app.py
from flask import Flask
import pika

app = Flask(__name__)
connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()

channel.queue_declare(queue='example-queue')

@app.route('/')
def consume_message():
    method_frame, header_frame, body = channel.basic_get(queue='example-queue')
    if method_frame:
        return f"Received message: {body}"
    else:
        return "No messages in the queue."

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def main():
#     return 'Display is working'