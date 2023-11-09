from flask import Flask
import pika

app = Flask(__name__)
connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()

channel.queue_declare(queue='example-queue')

@app.route('/')
def produce_message():
    channel.basic_publish(exchange='', routing_key='example-queue', body='Hello, RabbitMQ!')
    return 'Message sent to RabbitMQ queue.'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def main():
#     return 'Analyzer is working'