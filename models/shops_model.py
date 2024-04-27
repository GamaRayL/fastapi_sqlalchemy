from sqlalchemy import (
    Column,
    Integer,
    Text,
    String,
    Boolean,
    ForeignKey,
    CheckConstraint,
    SmallInteger,
)
from sqlalchemy.orm import relationship

from models import Base


class Shop(Base):
    __tablename__ = 'shops'

    id = Column(Integer(), primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    registration_address = Column(Text())
    logo_url = Column(Text())
    is_active = Column(Boolean(), default=False)
    user_id = Column(ForeignKey('users.id'))
    items = relationship('ShopItem', backref='shop')


class ShopItem(Base):
    __tablename__ = 'shop_items'

    id = Column(Integer, primary_key=True)
    quantity = Column(SmallInteger, default=1)
    shop_id = Column(ForeignKey('shops.id'))
    product_id = Column(ForeignKey('products.id'))
    product = relationship('Product')

    __table_args__ = (
        CheckConstraint('quantity >= 0', name='quantity_check')
    )
