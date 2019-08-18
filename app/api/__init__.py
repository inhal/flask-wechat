from flask import Blueprint

api = Blueprint('api', __name__, url_prefix='/v1')

from app.api.v1 import user
