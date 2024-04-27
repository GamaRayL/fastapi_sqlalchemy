from sqlalchemy import (
    Column,
    Integer,
    String,
    Numeric,
    Text,
    ForeignKey,
    CheckConstraint,
)
from sqlalchemy.orm import relationship

from models import Base


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    category_id = Column(ForeignKey('category.id'))
    name = Column(String(255), unique=True, nullable=False)
    description = Column(Text)
    article = Column(String(100), unique=True, nullable=False)
    barcode = Column(String(100), nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    quantity = Column(Integer, nullable=False)
    slug = Column(String(100), unique=True, nullable=False)
    image_url = Column(Text)
    category = relationship('Category', backref='product')

    __table_args__ = (
        CheckConstraint('price > 0', name='price_check'),
        CheckConstraint('quantity >= 0', name='quantity_check'),
    )
