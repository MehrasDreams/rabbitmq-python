import pika
import time

# Sender code 



credentials = pika.PlainCredentials('root', 'root')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))


ch = connection.channel()




ch.exchange_declare(exchange='direct_logs', exchange_type='direct')


result = ch.queue_declare(queue='', exclusive=True)



qname = result.method.queue



severity = 'error'



ch.queue_bind(exchange='direct_logs', queue=qname, routing_key=severity)





print('[+] Waiting for log ')





def callback(ch, method, properties, body):
    with open('error_logs.log', 'a') as el:
        el.write(str(body) + '\n')

ch.basic_consume(queue=qname, on_message_callback=callback, auto_ack=True)


ch.start_consuming()