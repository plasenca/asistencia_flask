import datetime

from app import app
from flask import flash
from flask import Markup
from flask import url_for
from flask import request
from flask import redirect
from flask import render_template
from constants import BASE_DIR, FILES_DIR
from psycopg2 import DatabaseError
from flask_login import login_user
from flask_login import current_user
from flask_login import logout_user
from flask_login import login_required
from werkzeug.utils import secure_filename
from models.models import FileLoader
from models.models import RegisterForms, Role
from models.models import LoginForm, PageRegisterForm
from utilities.utilities import DataConverter

# Base URL redirect to login 
@app.route('/')
def index():
    
    return redirect("login"), 302

@app.route('/register', methods=["GET", "POST"])
def registro():

    form = PageRegisterForm()
    if request.method == "POST":
        if form.validate_on_submit():

            register_user = {
                "email": form.email.data,
                "email_confirmed_at": datetime.datetime.now(),
                "password": form.password.data,
                "is_active": True,
                "first_name": form.first_name.data,
                "last_name": form.last_name.data,
                "work_site": form.work_site.data,
                "role_id": 2
            }
            
            # Verificando si el usuario ya ha sido creado
            user = RegisterForms.get_by_email(register_user["email"])
            if user is not None:
                error = Markup(f"El email \"<strong>{register_user['email']}</strong>\" ya está siendo usado por otro usuario")
                flash(error)
            else:
                user = RegisterForms(email=register_user["email"], 
                                    email_confirmed_at=register_user["email_confirmed_at"],
                                    password=register_user["password"],
                                    active=register_user["is_active"],
                                    first_name=register_user["first_name"],
                                    last_name=register_user["last_name"],
                                    work_site=register_user["work_site"],
                                    role_id=register_user["role_id"])
                user.set_password(register_user["password"])
                user.save()
                
                registration_success = "Registro Exitoso"
                flash(registration_success)
                return redirect(url_for("login")), 302
    return render_template('registro/registro.html', form=form), 200

@app.route('/login', methods=['GET', 'POST'])
def login():
    
    if current_user.is_authenticated:
        return redirect(url_for('main')), 302
    
    form = LoginForm()    

    if request.method == "POST":
        if form.validate_on_submit():
            
            login_user_dict = {
                "email"   : form.email.data,
                "password": form.password.data,
                "remember": form.remember.data
            }
            user = RegisterForms.get_by_email(login_user_dict["email"])
            # Si el correo no existe
            if user is None:
                error = f"Usuario no encontrado"
                flash(error)
            else:
                # Si la contraseña concuerda con la ingresada
                if user.check_password(login_user_dict["password"]):
                    login_user(user, remember=login_user_dict["remember"])
                    return redirect(url_for("main")), 302
                else: 
                    error = f"La contraseña ingresada es  inválida"
                    flash(error)
    return render_template('login/login.html', form=form, request=request), 200

@app.route('/main', methods=["GET"])
@login_required
def main():
    form = FileLoader()
    
    files = [f for f in FILES_DIR.iterdir()]
    file = files[0]
    file_csv = DataConverter.to_format_time(file, columns=["arrive_time"], format_time = "%Y-%m-%d %H:%M:%S")
    

    
    return render_template('main/main.html', form=form, file_csv=file_csv), 200

@app.route('/file-added', methods=["POST"])
@login_required
def file_added():
    form = FileLoader()
    if form.validate_on_submit():
        
        file = form.file.data
        # If it does exist any file
        if file:

            # Eliminar todos los ficheros antes de agregar otro
            files_in_files = FILES_DIR.glob("*.*")
            list(map(lambda f: f.unlink(), files_in_files))
            
            # Guardar el fichero enviado
            filename = secure_filename(file.filename)
            file.save(FILES_DIR/filename)
            return redirect(url_for("main")), 302
        
        # If it does not exist any file
        if file is None:
            not_file = "Does not exist any file to upload"
            flash(not_file, category="error")
            return redirect(url_for("main")), 302


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index")), 302

# Error Pages

@app.errorhandler(404)
def page_404(error):
    return render_template("errors/404.html"), 404

@app.errorhandler(DatabaseError)
def page_500(error):
    return render_template("errors/500.html"), 500


# Custom Filters

    # Custom Filter to convert str to datetime format
@app.template_filter('date')
def date_filter(s, format):
    return datetime.datetime.strptime(s, format)

    # Custom Filter to return the month form a datetime object
@app.template_filter('month')
def month_filter(s):
    return datetime.datetime.strftime(s, "%B")

    # 
@app.template_filter("strip")
def str_strip(s:str):
    return s.strip()