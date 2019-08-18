from wtforms import Form

from app.libs.exceptions import ParameterException


class BaseForm(Form):
    def __init__(self, data):
        super().__init__(data=data)

    def validate_for_api(self, msg=None):
        valid = super().validate()
        if not valid:
            if msg is not None:
                raise ParameterException(msg=msg)
            else:
                raise ParameterException(msg=self.errors)
