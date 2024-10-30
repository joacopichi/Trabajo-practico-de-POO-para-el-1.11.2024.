from flask import render_template, request, redirect, url_for, flash
from models.user_manager import UserManager
from . import login

user_manager = UserManager()

@login.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if user_manager.authenticate_user(username, password):
            flash('Inicio de sesión exitoso!')
            return redirect(url_for('login.index'))
        else:
            flash('Usuario o contraseña incorrectos')
    return render_template('login.html')

@login.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if not user_manager.register_user(username, password):
            flash('El usuario ya existe')
        else:
            flash('Registro exitoso! Ahora puedes iniciar sesión.')
            return redirect(url_for('login.login_page'))
    return render_template('register.html')