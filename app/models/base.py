from contextlib import contextmanager
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer


class SubSQLAlchemy(SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e


db = SubSQLAlchemy()


class BaseModel(db.Model):
    __abstract__ = True
    create_time = Column(Integer)

    def __init__(self):
        self.create_time = int(datetime.now().timestamp())

    def set_attrs(self, attr_dict):
        for key, value in attr_dict:
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)
