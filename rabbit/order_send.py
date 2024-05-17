import json

import pika

from rabbit.order_validation import order_validation, ValidationError


def order_send(_queue: str, new_order: dict):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    
    try:
        order_validation(new_order)
    except ValidationError as e:
        print(f'Ошибка валидации: {str(e)}')

    order_json = json.dumps(new_order)

    channel.queue_declare(queue=_queue, durable=True)

    channel.basic_publish(
        exchange='',
        routing_key=_queue,
        body=order_json.encode(),
        properties=pika.BasicProperties(
            delivery_mode=pika.DeliveryMode.Persistent
        )
    )
    print(f' [x] Отправлен: {order_json}')

    connection.close()
