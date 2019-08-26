from sqlalchemy import Column, Integer, String

from app.models.base import BaseModel


class User(BaseModel):
    id = Column(Integer, primary_key=True, autoincrement=True)
    openid = Column(String(50), nullable=False, unique=True)
