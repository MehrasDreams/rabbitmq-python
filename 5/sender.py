import pika
import time

# Sender code 



credentials = pika.PlainCredentials('root', 'root')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))


ch = connection.channel()



ch.exchange_declare(exchange='topic_logs', exchange_type='topic')




messages = {
    'error.warning.important': 'this is an important message',
    'info.debug.notimportant': 'this is not important message',

}


for k,v in messages.items():
    ch.basic_publish(exchange='topic_logs', routing_key=k, body=v)



print("[+] Sent")




ch.close()