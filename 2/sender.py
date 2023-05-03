import pika


# Sender code 



credentials = pika.PlainCredentials('root', 'root')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))


ch = connection.channel()


ch.queue_declare(queue='program', durable=True)




message = 'This is testing message'


ch.basic_publish(exchange='', routing_key='program', body=message, properties=pika.BasicProperties(delivery_mode=2,))  # delivery mode for hard and ram stuff




print("Send message ")





ch.close()