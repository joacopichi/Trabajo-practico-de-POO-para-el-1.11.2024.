import requests
import json

class ServicioPeliculas:
    def __init__(self, api_key=None):
        self.api_key = api_key  # Clave de la API
        self.base_url = "http://www.omdbapi.com/"
        self.peliculas_muestra = self.cargar_peliculas_muestra()

    def cargar_peliculas_muestra(self):
        with open('static/peliculas_muestra.json', 'r', encoding='utf-8') as file:
            return json.load(file)

    def buscar_pelicula(self, titulo):
        if self.api_key:  # Si se proporciona la clave de API
            params = {'t': titulo, 'apikey': self.api_key}
            response = requests.get(self.base_url, params=params)

            if response.status_code != 200:
                return None
            data = response.json()
            if data.get('Response') == 'False':
                return None
            return data
        else:  # Si no hay clave API, devolver una película de muestra
            for pelicula in self.peliculas_muestra:
                if pelicula['Title'].lower() == titulo.lower():
                    return pelicula
            return None

    def mostrar_datos(self, titulos):
        resultados = []
        for titulo in titulos:
            pelicula = self.buscar_pelicula(titulo)
            if pelicula:
                resultados.append(pelicula)
        return resultados