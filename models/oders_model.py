from sqlalchemy import (
    Column,
    Integer,
    Numeric
)

from .base import Base


class Order(Base):
    __tablename__ = 'orders'

    order_id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, nullable=False, unique=True)
    total_amount = Column(Numeric)
