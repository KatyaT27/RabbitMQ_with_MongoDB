import pika
from models import Contact

credentials = pika.PlainCredentials(username='rkiuojxv', password='zWn6xEcvVkmSYuES_VE-yW2HZTOM4aAT')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='sparrow-01.rmq.cloudamqp.com', port=5672, credentials=credentials, virtual_host='rkiuojxv'))
channel = connection.channel()

queue = channel.queue_declare(queue='', exclusive=True)

def send_email(email):
    # Simulate sending an email here
    print(f"Simulating email sent to {email}")

def callback(ch, method, properties, body):
    pk = body.decode()
    contact = Contact.objects(id=pk, email_sent=False).first()
    if contact:
        # Simulate sending an email
        send_email(contact.email)
        
        # Update the email_sent field
        contact.update(set__email_sent=True)

    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_campaing', on_message_callback=callback)

if __name__ == '__main__':
    channel.start_consuming()
