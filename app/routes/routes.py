from flask import render_template, redirect
from forms.forms import LoginForm
from app import app

@app.route('/')
def index():
    return redirect("login"), 302

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login/login.html', form=form), 200

@app.route('/main')
def main():
    return render_template('main/main.html'), 200

@app.route("/test")
def test():
    return render_template('main/asistencia.html'), 200