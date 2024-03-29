from decouple import config
import pika, sys, os

def main():
    credentials = pika.PlainCredentials(config('AMQP_USER'), config('AMQP_PASS'))
    parameters = pika.ConnectionParameters(host=config('AMQP_HOST'), port=config('AMQP_PORT'), virtual_host='/', credentials=credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)