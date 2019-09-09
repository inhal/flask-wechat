from app.libs.exception_handle import ExceptionHandle


class ParameterException(ExceptionHandle):
    code = 400
    msg = 'Parameter error'
    error_code = 4000


class WechatException(ExceptionHandle):
    code = 400
    msg = 'wechat unknown error'
    error_code = 4002


class TokenException(ExceptionHandle):
    code = 403
    msg = 'token verify failed'
    error_code = 4003
