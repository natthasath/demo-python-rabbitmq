from decouple import config
import pika, sys, os

credentials = pika.PlainCredentials(config('AMQP_USER'), config('AMQP_PASS'))
parameters = pika.ConnectionParameters(host=config('AMQP_HOST'), port=config('AMQP_PORT'), virtual_host='/', credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='logs', routing_key='', body=message)
print(" [x] Sent %r" % message)
connection.close()