from flask import render_template, request, redirect, url_for, flash
from . import login

users_db = {}

@login.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users_db and users_db[username] == password:
            flash('Inicio de sesión exitoso!', 'success')
            return redirect(url_for('login.index'))
        else:
            flash('Usuario o contraseña incorrectos', 'danger')
    return render_template('login.html')

@login.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users_db:
            flash('El usuario ya existe', 'danger')
        else:
            users_db[username] = password
            flash('Registro exitoso! Ahora puedes iniciar sesión.', 'success')
            return redirect(url_for('login.login_page'))
    return render_template('register.html')