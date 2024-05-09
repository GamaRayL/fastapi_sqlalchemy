from sqlalchemy.exc import IntegrityError

from database import SessionLocal
from models import Order
from .base import channel


def order_recieve(new_order: Order):
    channel.queue_declare(queue=new_order, durable=True)
    print(' [*] Ожидание сообщений. Для выхода нажмите CTRL+C')

    def callback(ch, method, properties, body: Order):
        print(f' [x] Получен "{body.__name__}"')
        session = SessionLocal()

        try:
            with session.begin():
                session.add(body)
                session.commit()
        except IntegrityError as e:
            print('Ошибка при выполнении операций с базой данных: ', e)

        print(session.query(Order.order_id, Order.total_amount).all())

        print(' [x] Готово')
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(
        queue=new_order,
        on_message_callback=callback
    )

    channel.start_consuming()
