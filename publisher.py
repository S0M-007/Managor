import pika

# Connect to RabbitMQ (adjust hostname, username, and password)
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='my_queue')
for i in range(50):
    message = f"Message {i}"
    channel.basic_publish(exchange='', routing_key='my_queue', body=message)
    print(f"Sent: {message}")

# Close the connection
connection.close()
