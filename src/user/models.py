from sqlalchemy import Column, String, Integer, Boolean, DateTime
from src.utils.db import Base

class User(Base):
    __tablename__= "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    username = Column(String, nullable=False)
    hash_password = Column(String, nullable=False)
    email = Column(String)