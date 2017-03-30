from sqlalchemy import Column, Integer, Text  
from .base import Base

class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    email = Column(Text)

    def serialize(self):
        return {
            "name": self.name,
            "email": self.email
        }