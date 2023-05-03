import pika
import time

# Sender code 



credentials = pika.PlainCredentials('root', 'root')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))


ch = connection.channel()



ch.exchange_declare(exchange='logs', exchange_type='fanout')






ch.basic_publish(exchange='logs', routing_key='', body="This is testing fanout")

print("Message sent")


ch.close()

