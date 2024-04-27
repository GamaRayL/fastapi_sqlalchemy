from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from settings import DATABASE_URL

Base = declarative_base()

engine = create_engine(DATABASE_URL)
