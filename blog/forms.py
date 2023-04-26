from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
from wtforms.validators import DataRequired, InputRequired
from wtforms.widgets import TextArea


class LoginForm(FlaskForm):
    username = StringField("Логин", validators=[DataRequired()])
    password = PasswordField("Пароль", validators=[DataRequired()])

class CommentForm(FlaskForm):
    text = StringField("Комментарий", validators=[InputRequired()], widget=TextArea())