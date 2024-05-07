from sqlalchemy import (
    Column,
    Integer,
    Numeric
)

from .base import Base


class BankAccount(Base):
    __tablename__ = 'bank_accounts'

    account_id = Column(Integer, primary_key=True)
    balance = Column(Numeric)
