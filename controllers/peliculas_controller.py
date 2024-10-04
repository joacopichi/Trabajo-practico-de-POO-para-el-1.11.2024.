from flask import Blueprint, render_template, request, redirect, url_for
from services.servicio_peliculas import ServicioPeliculas

# Definimos un Blueprint para las rutas relacionadas con películas
peliculas_bp = Blueprint('peliculas', __name__)

@peliculas_bp.route('/')
def index():
    return render_template('index.html')

@peliculas_bp.route('/buscar', methods=['POST'])
def buscar():
    consulta = request.form.get('consulta')
    
    if not consulta:
        return redirect(url_for('peliculas.index'))

    servicio_peliculas = ServicioPeliculas()
    
    try:
        pelicula = servicio_peliculas.buscar_pelicula(consulta)
        return render_template('resultados.html', pelicula=pelicula)
    except ValueError as e:
        return render_template('error.html', mensaje_error=str(e))
