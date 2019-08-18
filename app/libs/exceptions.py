from app.libs.exception_handle import ExceptionHandle


class ParameterException(ExceptionHandle):
    code = 400
    msg = 'Parameter error'
    error_code = 4000
