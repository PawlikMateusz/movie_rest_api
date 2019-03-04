import os
import requests
from django.http import request


API_KEY = os.getenv("API_KEY", None)


def fetch_movie_data(title):
    url = 'http://www.omdbapi.com/?t={0}&apikey={1}'.format(title, API_KEY)
    r = requests.get(url)
    movie = r.json()
    return movie
