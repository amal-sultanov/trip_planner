from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired('Заполните поле')])
    name = StringField('Name', validators=[DataRequired('Заполните поле')])
    email = EmailField('Email',
                       validators=[DataRequired('Заполните поле'), Email()])
    password = PasswordField('Password',
                             validators=[DataRequired('Заполните поле')])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[
                                         DataRequired('Заполните поле'),
                                         EqualTo('password')
                                     ])
    button = SubmitField('Register')


class LoginForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired('Заполните поле')])
    password = PasswordField('Password',
                             validators=[DataRequired('Заполните поле')])
    button = SubmitField('Login')
