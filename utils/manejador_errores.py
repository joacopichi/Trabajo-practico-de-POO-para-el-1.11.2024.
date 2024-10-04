from flask import render_template

def configurar_manejo_errores(app):
    @app.errorhandler(404)
    def pagina_no_encontrada(error):
        return render_template('error.html', mensaje_error="Página no encontrada."), 404

    @app.errorhandler(500)
    def error_interno(error):
        return render_template('error.html', mensaje_error="Error interno del servidor."), 500
