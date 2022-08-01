import email
from app import db
from flask_user import UserManager, UserMixin
from flask_wtf import FlaskForm
from wtforms import (EmailField, PasswordField,
                     SubmitField, BooleanField,
                     StringField)
from wtforms.validators import (DataRequired, Length, Email)
from app import login_manager

# CreatinG Users Models
    
    # Creating the RegisterForm class with db.Model
class RegisterForms(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    
    # User Autentication
    email = db.Column(db.Unicode(255), unique=True, nullable=False, server_default=u'')
    email_confirmed_at = db.Column(db.DateTime())
    password = db.Column(db.String(255), nullable=False, server_default='')
    active = db.Column(db.Boolean(), nullable=False, server_default='0')
    
    # User Information
    active = db.Column('is_active', db.Boolean(), nullable=False, server_default='0')
    first_name = db.Column(db.Unicode(50), nullable=False, server_default=u'')
    last_name = db.Column(db.Unicode(50), nullable=False, server_default=u'')
    
    # Relationships
    roles = db.relationship('Role', secondary='user_roles', 
                            backref= db.backref('users', lazy='dynamic'))


    # Creating the Role class with db.Model
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), nullable=False, server_default='', unique=True) # for @roles_accepted()
    label = db.Column(db.Unicode(255), nullable=False, server_default='')
    
    
    # Creating the UserRoles class with db.Model
class UserRoles(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'))


# Creating Forms

    # Creating the LoginForm class with FlaskForm
class LoginForm(FlaskForm):
    email = EmailField('Email Addres', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    login = SubmitField('Sign In')
    remember = BooleanField('Remember Me')


    # Creating the RegisterForm class with FlaskForm
class RegisterForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(1, 50)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(1, 50)])
    email = EmailField('Email Address', validators=[DataRequired(), Length(1, 64), Email()])
    email_confirmer = EmailField('Confirm Email', validators=[DataRequired(), Length(1, 64), Email()])
    agree_to_terms = BooleanField('Agree to Terms', validators=[DataRequired()])
    register = SubmitField('Register')

@login_manager.user_loader
def load_user(email):
    return LoginForm.get(email)