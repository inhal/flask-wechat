from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer

db = SQLAlchemy()


class BaseModel(db.Model):
    __abstract__ = True
    create_time = Column(Integer)

from app.models import user
