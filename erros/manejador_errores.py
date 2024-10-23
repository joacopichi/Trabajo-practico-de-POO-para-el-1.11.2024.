def configurar_manejo_errores(app):
    @app.errorhandler(404)
    def pagina_no_encontrada(e):
        return {"error": "Página no encontrada"}, 404

    @app.errorhandler(500)
    def error_interno(e):
        return {"error": "Error interno del servidor"}, 500