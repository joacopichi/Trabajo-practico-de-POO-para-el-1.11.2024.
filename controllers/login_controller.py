from flask import Blueprint, render_template, redirect, url_for, request, flash, session

login_bp = Blueprint('login', __name__)

usuarios = {}

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username in usuarios and usuarios[username] == password:
            session['username'] = username
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('peliculas.index'))
        else:
            flash('Credenciales incorrectas', 'danger')
    
    return render_template('login.html')

@login_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username in usuarios:
            flash('El usuario ya existe', 'danger')
        else:
            usuarios[username] = password
            flash('Registro exitoso', 'success')
            return redirect(url_for('login.login'))

    return render_template('register.html')