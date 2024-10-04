import os

class Config:
    OMDB_API_KEY = os.getenv('OMDB_API_KEY', 'tu_clave_api_aqui')
