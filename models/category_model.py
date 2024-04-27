from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    ForeignKey
)

from .base import Base


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    parent_category = Column(ForeignKey('category.id'))
    description = Column(Text)
