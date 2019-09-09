import datetime

import jwt
from flask import current_app, request
from jwt import ExpiredSignatureError, InvalidIssuedAtError, InvalidSignatureError

from app.libs.exceptions import WechatException, TokenException
from app.models.user import User
from app.utils.httper import HTTP


def issue_token(code):
    openid = _get_openid(code)
    user_id = _is_register(openid)
    token = _make_token(user_id)
    return token


def verify():
    token = request.headers['token']
    app = current_app
    key = app.config['JWT_KEY']
    try:
        r = jwt.decode(token, key, algorithm='HS256')
        if r:
            return True
    except Exception as e:
        # print(e.__class__.__name__)
        if isinstance(e, InvalidSignatureError) or isinstance(e, InvalidIssuedAtError):
            raise TokenException(msg='token不合法')
        elif isinstance(e, ExpiredSignatureError):
            raise TokenException(msg='token已过期')


def _get_openid(code):
    app = current_app
    appid = app.config['APPID']
    appsecret = app.config['APPSECRET']
    login_url = app.config['LOGIN_URL'].format(appid, appsecret, code)
    wx_result = HTTP.get(login_url)
    if 'errcode' in wx_result:
        raise WechatException(msg=wx_result['errmsg'], error_code=wx_result['errcode'])
    return wx_result['openid']


def _is_register(openid):
    user_model = User()
    user = user_model.find_by_openid(openid)
    if user:
        return user.id
    else:
        register_user = user_model.register(openid)
        return register_user.id


def _make_token(user_id):
    app = current_app
    payload = {
        'uid': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=7200)
    }
    key = app.config['JWT_KEY']
    encoded_jwt = jwt.encode(payload, key, algorithm='HS256')
    return encoded_jwt
