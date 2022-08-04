from flask import (render_template, redirect, request, 
                   flash, Markup, url_for)
from models.models import LoginForm, PageRegisterForm
from models.models import RegisterForms, Role
from flask_login import login_user, current_user,login_required
from datetime import datetime
from app import app

@app.route('/')
def index():
    return redirect("login"), 302

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == "GET":
        return render_template('login/login-after-register.html', form=form), 200

    if request.method == "POST":
        if form.validate_on_submit():
            return redirect(url_for("main")), 302
    return render_template('login/login.html', form=form), 200

@app.route('/register', methods=["GET", "POST"])
def registro():
    # if current_user.is_authenticated():
    #     return render_template('registro/registro.html', form=form), 200
    form = PageRegisterForm()
    if request.method == "POST":
        if form.validate_on_submit():

            register_user = {
                "email": form.email.data,
                "email_confirmed_at": datetime.now(),
                "password": form.password.data,
                "is_active": True,
                "first_name": form.first_name.data,
                "last_name": form.last_name.data,
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
                                    role_id=register_user["role_id"])
                user.set_password(register_user["password"])
                user.save()
                
                registration_success = "Registro Exitoso"
                flash(registration_success)
                return redirect(url_for("login")), 302
    return render_template('registro/registro.html', form=form), 200


@app.route('/main', methods=["GET"])
@login_required
def main():
    return render_template('main/asistencia.html'), 200