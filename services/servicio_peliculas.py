import requests
from models.pelicula import Pelicula
from config import Config

class ServicioPeliculas:
    def __init__(self):
        self.api_key = Config.OMDB_API_KEY
        self.base_url = "http://www.omdbapi.com/"

    def buscar_pelicula(self, titulo):
        params = {
            't': titulo,
            'apikey': self.api_key
        }
        response = requests.get(self.base_url, params=params)

        if response.status_code != 200:
            raise ValueError("Error al conectar con el servicio de películas.")

        data = response.json()

        if data.get('Response') == 'False':
            raise ValueError(f"No se encontró la película: {titulo}")

        pelicula = Pelicula(
            titulo=data.get('Title'),
            anio=data.get('Year'),
            duracion=data.get('Runtime'),
            director=data.get('Director'),
            sinopsis=data.get('Plot')
        )

        return pelicula
