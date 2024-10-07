import os

class Config:
    TMDB_API_KEY  = os.getenv('TMDB_API_KEY ', 'tu_clave_api_aqui')
