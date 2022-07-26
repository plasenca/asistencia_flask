import email
from flask_wtf import FlaskForm
from wtforms import (EmailField, PasswordField,
                     SubmitField, BooleanField)
from wtforms.validators import (DataRequired, Length, Email)
from app import login_manager


class LoginForm(FlaskForm):
    email = EmailField('Email Addres', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    login = SubmitField('Sign In')
    remember = BooleanField('Remember Me')
    

@login_manager.user_loader
def load_user(user_id):
    return LoginForm.get(email)