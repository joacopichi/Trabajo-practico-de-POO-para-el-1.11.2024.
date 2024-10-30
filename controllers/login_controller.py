from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from models.user_manager import UserManager

login_bp = Blueprint('login', __name__)
user_manager = UserManager()

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if user_manager.authenticate_user(username, password):
            session['username'] = username
            flash('Inicio de sesión exitoso')
            return redirect(url_for('peliculas.index'))
        else:
            flash('Credenciales incorrectas')
    
    return render_template('login.html')

@login_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not user_manager.register_user(username, password):
            flash('El usuario ya existe')
        else:
            flash('Registro exitoso')
            return redirect(url_for('login.login'))

    return render_template('register.html')