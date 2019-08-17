from app.api import api
from app.libs.exception_handle import ExceptionHandle

user = api


@user.route('/v1/user/show')
def show():
    raise ExceptionHandle(404, 'not fond', 1001)
