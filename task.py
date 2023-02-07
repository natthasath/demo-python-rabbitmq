from decouple import config
import pika, sys, os

credentials = pika.PlainCredentials(config('AMQP_USER'), config('AMQP_PASS'))
parameters = pika.ConnectionParameters(host=config('AMQP_HOST'), port=config('AMQP_PORT'), virtual_host='/', credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='', routing_key='hello', body=message)
print(" [x] Sent %r" % message)
connection.close()