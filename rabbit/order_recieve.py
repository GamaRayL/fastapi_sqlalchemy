import json
import sys
import traceback

import pika
from sqlalchemy.exc import IntegrityError

from database.session import SessionLocal
from models import Order
from rabbit.order_validation import order_validation, ValidationError


def order_recieve(_queue: str):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue=_queue, durable=True)
    session = SessionLocal()
    print(' [*] Ожидание сообщений. Для выхода нажмите CTRL+C')

    def callback(ch, method, properties, body):
        new_order = json.loads(body.decode())
        try:
            order_validation(new_order)
        except ValidationError as e:
            print(f'Ошибка валидации: {str(e)}')

        customer_id = new_order.get('customer_id')
        total_amount = new_order.get('total_amount')

        try:
            new_order = Order(
                customer_id=customer_id,
                total_amount=total_amount
            )
            session.add(new_order)
            session.commit()
            print(f'Транзакция прошла успешно. Заказ с {new_order} добавлен в базу')
        except IntegrityError as e:
            print('Ошибка при выполнении операций с базой данных: ', e)
            session.rollback()

        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(
        queue=_queue,
        on_message_callback=callback,
    )

    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()
    except Exception:
        traceback.print_exc(file=sys.stdout)
        channel.stop_consuming()
    finally:
        session.close()
