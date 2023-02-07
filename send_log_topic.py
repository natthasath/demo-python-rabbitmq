from decouple import config
import pika, sys, os

credentials = pika.PlainCredentials(config('AMQP_USER'), config('AMQP_PASS'))
parameters = pika.ConnectionParameters(host=config('AMQP_HOST'), port=config('AMQP_PORT'), virtual_host='/', credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

routing_key = sys.argv[1] if len(sys.argv) > 2 else 'anonymous.info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'
channel.basic_publish(exchange='topic_logs', routing_key=routing_key, body=message)
print(" [x] Sent %r:%r" % (routing_key, message))
connection.close()