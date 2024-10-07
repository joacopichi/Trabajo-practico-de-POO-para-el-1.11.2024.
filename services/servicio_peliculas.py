import requests

class ServicioPeliculas:
    def __init__(self):
        self.api_key = 'trilogy'  # Clave pública gratuita para OMDb
        self.base_url = "http://www.omdbapi.com/"

    def buscar_pelicula(self, titulo):
        params = {
            't': titulo,
            'apikey': self.api_key
        }
        
        response = requests.get(self.base_url, params=params)

        if response.status_code != 200:
            print("Error al conectar con el servicio de películas.")
            return None

        data = response.json()

        if data.get('Response') == 'False':
            print(f"No se encontró la película: {titulo}")
            return None

        return data  # Retorna los datos de la película

    def mostrar_datos(self, titulos):
        for titulo in titulos:
            print(f"Buscando: {titulo}")
            pelicula = self.buscar_pelicula(titulo)
            if pelicula:
                print(f"Título: {pelicula['Title']}")
                print(f"Año: {pelicula['Year']}")
                print(f"Duración: {pelicula['Runtime']}")
                print(f"Director: {pelicula['Director']}")
                print(f"Sinopsis: {pelicula['Plot']}")
                print(f"Clasificación: {pelicula['Rated']}")
                print("-------------")

# Ejemplo de uso
if __name__ == '__main__':
    servicio = ServicioPeliculas()
    titulos_a_buscar = ["Inception", "Titanic", "Avatar", "The Matrix", "Interstellar"]
    servicio.mostrar_datos(titulos_a_buscar)
