#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello',durable=True)

channel.basic_publish(exchange='', routing_key='hello', body='Selamat Pagi')
print(" [x] Sent 'Selamat Pagi'")
connection.close()