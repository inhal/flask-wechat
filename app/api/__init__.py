from flask import Blueprint

api = Blueprint('api', __name__, url_prefix='/api/v1')

from app.api.v1 import auth

from app.models.user import User
