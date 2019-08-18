import json

from flask import request
from werkzeug.exceptions import HTTPException


class ExceptionHandle(HTTPException):
    """自定义 HTTP 异常处理基类
    返回格式 json 数据
    格式为： {msg: '', error_code: 999, request: 'GET/POST /example/example'}
        msg: 错误信息
        error_code: 自定义错误码，参照项目根目录 error_code.md 文件
        request: 请求 url。前面为 HTTP 动词，后面为不带参数 url
    """
    code = 500  # HTTP状态码
    msg = 'sorry, we make a mistake.'
    error_code = 999  # 自定义错误码

    def __init__(self, code=None, msg=None, error_code=None):
        if code is not None:
            self.code = code
        if msg is not None:
            self.msg = msg
        if error_code is not None:
            self.error_code = error_code
        super().__init__(self.msg, None)

    def get_headers(self, environ=None):
        return [("Content-Type", "application/json")]

    def get_body(self, environ=None):
        body = dict(
            msg=self.msg,
            error_code=self.error_code,
            request=request.method + ' ' + self.remove_url_params()
        )
        return json.dumps(body)

    @staticmethod
    def remove_url_params():
        """ 移除url中的含参部分 """
        full_path = request.full_path
        main_path = full_path.split('?')[0]
        return main_path
