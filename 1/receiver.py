import pika


# Sender code 



credentials = pika.PlainCredentials('root', 'root')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))



def return_as_text(ch, method, properties, body):
    print(f'Recevied body: {body}')



ch2 = connection.channel()
ch2.queue_declare(queue='hello')


ch2.basic_consume(queue='hello', on_message_callback=return_as_text, auto_ack=True)



print("Press crtl + c to exit")


ch2.start_consuming()

