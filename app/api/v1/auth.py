import json

from flask import request, jsonify

from app.api import api
from app.libs.exceptions import ParameterException
from app.sevice import token
from app.validator.forms import AuthForm


@api.route('/auth', methods=['POST'])
def issue_token():
    data = request.json
    form = AuthForm(data=data)
    if form.validate():
        user_token = _issue_token(form)
        r = {
            'token': str(user_token, encoding="utf-8")
        }
        print(type(r))
        return jsonify(r)
    else:
        raise ParameterException(msg=form.errors)


@api.route('/auth/verify')
def verify_token():
    verify_res = token.verify()
    if verify_res:
        return jsonify({'verify': True})


def _issue_token(form):
    code = form.data['code']
    user_token = token.issue_token(code)
    return user_token
