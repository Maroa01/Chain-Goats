import datetime
from typing import List
from uuid import uuid4

from app.database import Base
from sqlalchemy import Boolean,TIMESTAMP, Column, ForeignKey, Integer, String, text
from sqlalchemy.orm import relationship
from app.utils import hashing


class User(Base):
    __tablename__ = "users"

    id = Column("user_id", String(64), primary_key=True,
                index=True, default=uuid4)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)

    def __init__(self, name, email, password, *args, **kwargs):
        self.name = name
        self.email = email
        self.password = hashing.get_password_hash(password)

    def check_password(self, password):
        return hashing.verify_password(self.password, password)
