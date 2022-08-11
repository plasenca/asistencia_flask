from app import db
from app import login_manager, app
from flask_wtf import FlaskForm
from flask_user import UserMixin
from flask_user import UserManager
from wtforms import EmailField
from wtforms import SubmitField
from wtforms import StringField
from wtforms import SelectField
from wtforms import BooleanField
from wtforms import PasswordField
from wtforms.validators import Email
from wtforms.validators import Length
from wtforms.validators import EqualTo
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

# CreatinG Users Models

    # Creating the RegisterForm class with db.Model
class RegisterForms(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)

    # User Autentication
    email = db.Column(db.Unicode(255), unique=True,
                      nullable=False, server_default=u'')
    email_confirmed_at = db.Column(db.DateTime())
    password = db.Column(db.String(255), nullable=False, server_default='')
    active = db.Column(db.Boolean(), nullable=False, server_default='0')

    # User Information
    active = db.Column('is_active', db.Boolean(),
                        nullable=False, server_default='0')
    first_name = db.Column(db.Unicode(50), nullable=False, server_default=u'')
    last_name = db.Column(db.Unicode(50), nullable=False, server_default=u'')

    # Relationships
    work_id = db.Column(db.Integer, db.ForeignKey("locations.id"))
    role_id = db.Column(db.Integer,  db.ForeignKey("roles.id"))
    
    def __repr__(self) -> str:
        return f'<User {self.first_name} {self.last_name}>'

    def set_password(self, password):
        self.password = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def save(self:"RegisterForms"):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_by_id(_id:int) -> str:
        return RegisterForms.query.get(_id).first()
    
    @staticmethod
    def get_by_email(email:str):
        return RegisterForms.query.filter_by(email=email).first()

    # Creating the Role class with db.Model

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), nullable=False,
                    server_default='', unique=True)  # for @roles_accepted()
    label = db.Column(db.Unicode(255), nullable=False, server_default='')
    users = db.relationship("RegisterForms", backref=db.backref("roles"))


    # Creating the Location class with db.Model

class Location(db.Model):
    __tablename__ = "locations"
    
    id    = db.Column(db.Integer, primary_key=True)
    place = db.Column(db.String(50), nullable=False,
                    server_default='',unique=True)
    users = db.relationship("RegisterForms", backref=db.backref("location"))
    
    
# Creating Forms

    # Creating the LoginForm class with FlaskForm
class LoginForm(FlaskForm):
    email = EmailField('Email Addres', validators=[
                        DataRequired(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    login = SubmitField('Sign In')
    remember = BooleanField('Remember Me')

    # Creating the RegisterForm class with FlaskForm


class PageRegisterForm(FlaskForm):
    first_name = StringField('First Name',
                              validators=[DataRequired(),
                                        Length(1, 50)])
    last_name = StringField('Last Name',
                            validators=[DataRequired(),
                                        Length(1, 50)])
    email = EmailField('Email Address',
                        validators=[DataRequired(),
                                    Length(1, 64)])
    password = PasswordField("Password",
                            validators=[DataRequired(),
                                        EqualTo("password_confirmer", message="Las contraseñas deben coincidir")])
    password_confirmer = PasswordField('Repeat Password')
    agree_to_terms = BooleanField('Agree to Terms', validators=[DataRequired()])
    work_id = SelectField("Tienda", choices=[(1, "Oficina Principal"),
                                            (2, "Tienda Nicollini"),
                                            (3, "Tienda Ferretero")])
    register = SubmitField()


    # Creating form for upload a file

class FileLoader(FlaskForm):
    file = FileField(label="Export")
    submit = SubmitField()

# Configurations

@login_manager.user_loader
def load_user(id):
    return RegisterForms.query.get(int(id))

user_manager = UserManager(app, db, RegisterForms)