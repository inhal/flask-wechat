from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

from app.validator.base import BaseForm


class AuthForm(BaseForm):
    code = StringField(validators=[DataRequired()])

