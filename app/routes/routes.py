from flask import render_template, redirect, request
from models.models import LoginForm, PageRegisterForm
from flask_login import login_user
from app import app

@app.route('/')
def index():
    return redirect("login"), 302

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == "POST":
        print(form.validate_on_submit())
        if form.validate_on_submit():
            return render_template('main/asistencia.html', form=form), 200
    return render_template('login/login.html', form=form), 200

@app.route('/registro', methods=["GET", "POST"])
def registro():
    form = PageRegisterForm()
    if request.method == "POST":
        if form.validate_on_submit():
            return """<h1>Validado</h1>"""  
    return render_template('registro/registro.html', form=form), 200

@app.route('/main', methods=["GET"])
def main():
    return render_template('main/asistencia.html'), 200