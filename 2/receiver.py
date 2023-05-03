import pika
import time

# Sender code 



credentials = pika.PlainCredentials('root', 'root')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))



ch = connection.channel()

ch.queue_declare(queue='program', durable=True)


print("Waiting for message press ctrl + c to exit ")





def callback(ch, method, properties, body):
    print(f'Received {body}')
    time.sleep(9)
    print('Done')
    ch.basic_ack(delivery_tag=method.delivery_tag)


ch.basic_qos(prefetch_count=1)
ch.basic_consume(queue='program', on_message_callback=callback)



ch.start_consuming()