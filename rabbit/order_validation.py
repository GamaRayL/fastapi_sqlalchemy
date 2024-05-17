class ValidationError(Exception):
    pass


def order_validation(order):
    try:
        customer_id = order.get('customer_id')
        total_amount = order.get('total_amount')

        if not isinstance(customer_id, int):
            raise ValidationError('customer_id должен быть целым числом')

        if not isinstance(total_amount, (int, float)):
            raise ValidationError('total_amount должен быть числом')

        return True

    except Exception as e:
        return ValidationError(str(e))
