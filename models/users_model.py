from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from models import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    first_name = Column(String(255))
    last_name = Column(String(255))
    phone_number = Column(String(255))
    created_at = Column(DateTime, default=datetime.now())
    fav_product = Column(Integer, ForeignKey('products.id'))
    is_active = Column(Boolean, default=True)
    products = relationship('Product')
