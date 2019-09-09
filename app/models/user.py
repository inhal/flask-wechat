from flask_sqlalchemy import BaseQuery
from sqlalchemy import Column, Integer, String

from app.models.base import BaseModel, db


class User(BaseModel):
    id = Column(Integer, primary_key=True, autoincrement=True)
    openid = Column(String(50), nullable=False, unique=True)

    @staticmethod
    def register(openid):
        user = User()
        with db.auto_commit():
            user.openid = openid
            db.session.add(user)
        return user

    @staticmethod
    def find_by_openid(openid):
        user_id = User.query.filter_by(openid=openid).first()
        return user_id
