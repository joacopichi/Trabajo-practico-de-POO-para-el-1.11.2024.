from flask import Flask
from controllers.peliculas_controller import peliculas_bp
from controllers.login_controller import login_bp
from utils.manejador_errores import configurar_manejo_errores

app = Flask(__name__)

app.secret_key = 'tu_clave_secreta_aqui'

app.register_blueprint(peliculas_bp)
app.register_blueprint(login_bp)

configurar_manejo_errores(app)

if __name__ == '__main__':
    app.run(debug=True)