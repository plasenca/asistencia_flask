from flask import render_template, redirect
from app import app

@app.route('/')
def main():
    return redirect("login"), 302

@app.route('/login')
def login():
    return render_template('login/login.html'), 200