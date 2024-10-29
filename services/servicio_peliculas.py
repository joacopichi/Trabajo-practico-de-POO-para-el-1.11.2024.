import requests
import json

class ServicioPeliculas:
    _instance = None

    def __new__(cls, api_key=None):
        if not cls._instance:
            cls._instance = super(ServicioPeliculas, cls).__new__(cls)
            cls._instance.api_key = api_key
            cls._instance.base_url = "http://www.omdbapi.com/"
            cls._instance.peliculas_muestra = cls._instance.cargar_peliculas_muestra()
        return cls._instance

    def cargar_peliculas_muestra(self):
        try:
            with open('static/peliculas_muestra.json', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            print("El archivo 'peliculas_muestra.json' no se encontró.")
            return []

    def buscar_pelicula(self, titulo):
        if self.api_key:
            params = {'t': titulo, 'apikey': self.api_key}
            response = requests.get(self.base_url, params=params)

            if response.status_code != 200:
                return None
            data = response.json()
            if data.get('Response') == 'False':
                return None
            return data
        else:
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