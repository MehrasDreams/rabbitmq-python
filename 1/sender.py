import pika


# Sender code 



credentials = pika.PlainCredentials('root', 'root')

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))



channel = connection.channel()


channel.queue_declare(queue='hello')





channel.basic_publish(routing_key='hello', exchange='', body='Hello World')

print('message sent')
 

channel.close()