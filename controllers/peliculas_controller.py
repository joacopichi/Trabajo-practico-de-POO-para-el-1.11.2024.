from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from services.servicio_peliculas import ServicioPeliculas

peliculas_bp = Blueprint('peliculas', __name__)
servicio_peliculas = ServicioPeliculas() 

@peliculas_bp.route('/')
def login():
    return render_template('login.html')

@peliculas_bp.route('/index')
def index():
    if 'username' not in session:
        return redirect(url_for('peliculas.login'))
    return render_template('index.html')

@peliculas_bp.route('/buscar', methods=['POST'])
def buscar():
    consulta = request.form.get('consulta')

    if not consulta:
        flash('Por favor, ingresa un término de búsqueda')
        return redirect(url_for('peliculas.index'))

    pelicula = servicio_peliculas.buscar_pelicula(consulta)

    if not pelicula:
        titulos_muestra = ["Inception", "Titanic", "Avatar", "The Matrix", "Interstellar"]
        peliculas_muestra = [servicio_peliculas.buscar_pelicula(titulo) for titulo in titulos_muestra]
        flash('No se encontraron resultados para tu búsqueda. Mostrando películas de muestra.')
        return render_template('resultados.html', peliculas=peliculas_muestra)

    return render_template('resultados.html', pelicula=pelicula)