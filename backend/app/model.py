import datetime
from typing import List
from uuid import uuid4

from database import Base
from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String, text
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"


    id = Column("user_id", String(64), primary_key=True, index=True, default=str(uuid4))
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
