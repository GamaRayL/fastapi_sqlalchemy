from sqlalchemy import create_engine

from models.base import Base
from settings import DATABASE_URL

engine = create_engine(DATABASE_URL)

Base.metadata.create_all(engine)

print(Base)
