import pika

from models import Order
from .base import connection, channel


def order_send(_queue: str, obj: Order):
    channel.queue_declare(queue=_queue, durable=True)

    channel.basic_publish(
        exchange='',
        routing_key=_queue,
        body=obj,
        properties=pika.BasicProperties(
            delivery_mode=pika.DeliveryMode.Persistent
        )
    )
    print(f' [x] Отправлено: {obj.__name__}')

    connection.close()
