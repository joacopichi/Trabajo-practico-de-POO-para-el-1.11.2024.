from flask import Flask
from controllers.peliculas_controller import peliculas_bp
from utils.manejador_errores import configurar_manejo_errores

app = Flask(__name__)

# Registramos el blueprint del controlador de películas
app.register_blueprint(peliculas_bp)

# Configuramos el manejo de errores
configurar_manejo_errores(app)

if __name__ == '__main__':
    app.run(debug=True)
