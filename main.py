from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

from models import Base, Order
from settings import DATABASE_URL

engine = create_engine(DATABASE_URL)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()

try:
    with session.begin():
        new_order = Order(customer_id=5, total_amount=400)
        session.add(new_order)
        session.commit()
except IntegrityError as e:
    session.rollback()
    print('Ошибка при выполнении операций с базой данных: ', e)

print(session.query(Order.order_id, Order.total_amount).all())
