import json
import random
from faker import Faker
from models import Contact


import pika

fake = Faker()

credentials = pika.PlainCredentials(username='rkiuojxv', password='zWn6xEcvVkmSYuES_VE-yW2HZTOM4aAT')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='sparrow-01.rmq.cloudamqp.com', port=5672, credentials=credentials, virtual_host='rkiuojxv'))
channel = connection.channel()

channel.exchange_declare(exchange='task_service', exchange_type='direct')
channel.queue_declare(queue='task_campaing', durable=True)
channel.queue_bind(exchange='task_service', queue='task_campaing')

def create_fake_contact():
    return {
        "full_name": fake.name(),
        "email": fake.email(),
        "email_sent": False
    }

def main():
    # Generate fake contacts and save them to the MongoDB database
    num_contacts = 10  # You can change the number of contacts you want to generate
    for _ in range(num_contacts):
        fake_contact = create_fake_contact()
        contact = Contact(**fake_contact)
        contact.save()

        # Publish the contact's ID to RabbitMQ
        channel.basic_publish(
            exchange='task_service',
            routing_key='task_campaing',
            body=str(contact.id),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ))
        print(f"Created and published contact: {contact.full_name}")

    connection.close()

if __name__ == '__main__':
    main()
