from flask import request

from app.api import api
from app.validator.forms import LoginForm

user = api


@user.route('/user/login', methods=['POST'])
def login():
    data = request.json
    form = LoginForm(data=data)
    form.validate_for_api()
    return form.data
