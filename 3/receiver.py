import pika
import time

# Sender code 



credentials = pika.PlainCredentials('root', 'root')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))



ch = connection.channel()


ch.exchange_declare(exchange='logs', exchange_type='fanout')


result = ch.queue_declare(queue='', exclusive=True)
qname = result.method.queue


ch.queue_bind(exchange='logs', queue=qname)




print("Waiting for lgos")

def callback(ch, method, properties, body):
    print(f'Received {body}')


ch.basic_consume(qname, on_message_callback=callback, auto_ack=True)
ch.start_consuming()
