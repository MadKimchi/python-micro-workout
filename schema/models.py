from sqlalchemy import Column, Integer, String

from . import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(150))
    last_name = Column(String(150))
    username = Column(String(150))
    email = Column(String(150))
    password = Column(String(150))
