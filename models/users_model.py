from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    Table,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from models import Base

favourite_products = Table(
    'user_product', Base.metadata,
    Column('user_id', Integer(), ForeignKey('users.id')),
    Column('product_id', Integer(), ForeignKey('products.id'))
)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    first_name = Column(String(255))
    last_name = Column(String(255))
    phone_number = Column(String(255))
    created_at = Column(DateTime, default=datetime.now())
    is_active = Column(Boolean, default=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    product = relationship('Product', secondary=favourite_products, backref='user')
