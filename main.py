from models import Order
from rabbit.order_send import order_send

try:
    new_order = Order(customer_id=5, total_amount=1)
    order_send('new_orders', new_order)
except ValueError as e:
    print(f'Ошибка при создании объекта модели Order {e}')
