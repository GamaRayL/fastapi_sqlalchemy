from rabbit.order_send import order_send


def create_order():
    input_customer_id = input('ID пользователя ')
    input_total_amount = input('Стоимость ')
    new_order = {
        'customer_id': input_customer_id,
        'total_amount': input_total_amount
    }

    order_send('new_orders', new_order)


if __name__ == '__main__':
    create_order()
