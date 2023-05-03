import pika
import time

# Sender code 



credentials = pika.PlainCredentials('root', 'root')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))


ch = connection.channel()



ch.exchange_declare(exchange='direct_logs', exchange_type='direct')



messages = {
    'info': 'This is info message',
    'error': 'This is error message',
    'warning': 'This is warning message',

}


for k,v in messages.items():
    ch.basic_publish(exchange='direct_logs', routing_key=k, body=v)

