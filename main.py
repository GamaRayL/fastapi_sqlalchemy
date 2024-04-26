from sqlalchemy import create_engine

from models import Base
from settings import DATABASE_URL

engine = create_engine(DATABASE_URL)

Base.metadata.create_all(engine)
