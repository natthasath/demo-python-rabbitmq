from decouple import config
import pika, sys, os

credentials = pika.PlainCredentials(config('AMQP_USER'), config('AMQP_PASS'))
parameters = pika.ConnectionParameters(host=config('AMQP_HOST'), port=config('AMQP_PORT'), virtual_host='/', credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='logs', queue=queue_name)

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for logs. To exit press CTRL+C')
channel.start_consuming()