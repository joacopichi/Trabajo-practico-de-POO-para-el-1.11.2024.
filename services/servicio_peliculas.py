import requests
import json
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class ServicioPeliculas:
    _instance = None

    def __new__(cls, api_key=None):
        if not cls._instance:
            cls._instance = super(ServicioPeliculas, cls).__new__(cls)
            cls._instance.api_key = api_key
            cls._instance.base_url = "http://www.omdbapi.com/"
            cls._instance.peliculas_muestra = cls._instance.cargar_peliculas_muestra()
            logging.info("Instancia de ServicioPeliculas creada.")
        return cls._instance

    def cargar_peliculas_muestra(self):
        try:
            with open('static/peliculas_muestra.json', encoding='utf-8') as file:
                logging.info("Películas de muestra cargadas con éxito.")
                return json.load(file)
        except FileNotFoundError:
            logging.error("El archivo 'peliculas_muestra.json' no se encontró.")
            return []

    def buscar_pelicula(self, titulo):
        logging.info(f"Buscando película: {titulo}")
        if self.api_key:
            params = {'t': titulo, 'apikey': self.api_key}
            response = requests.get(self.base_url, params=params)

            if response.status_code != 200:
                logging.error(f"Error en la búsqueda de la película: {titulo}. Código de estado: {response.status_code}")
                return None
            
            data = response.json()
            if data.get('Response') == 'False':
                logging.warning(f"La película '{titulo}' no fue encontrada.")
                return None
            
            logging.info(f"Película '{titulo}' encontrada con éxito.")
            return data
        else:
            for pelicula in self.peliculas_muestra:
                if pelicula['Title'].lower() == titulo.lower():
                    logging.info(f"Película '{titulo}' encontrada en la lista de muestra.")
                    return pelicula
            
            logging.warning(f"La película '{titulo}' no fue encontrada en la lista de muestra.")
            return None

    def mostrar_datos(self, titulos):
        resultados = []
        for titulo in titulos:
            pelicula = self.buscar_pelicula(titulo)
            if pelicula:
                resultados.append(pelicula)
        
        logging.info(f"Datos de {len(resultados)} películas mostrados.")
        return resultados