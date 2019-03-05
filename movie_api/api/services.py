import os
import requests
from django.http import request
from rest_framework.response import Response
from rest_framework import status

from .models import Movie


API_KEY = os.getenv("API_KEY", None)


def fetch_and_validate_movie(title):
    url = 'http://www.omdbapi.com/?t={0}&apikey={1}'.format(title, API_KEY)
    r = requests.get(url)
    movie = r.json()
    if movie['Response'] == 'False':
        return Response(movie, status=status.HTTP_400_BAD_REQUEST)
    if Movie.objects.filter(imdbID=movie['imdbID']):
        return Response({'Error': "This movie already exist in Database"},
                        status=status.HTTP_400_BAD_REQUEST)
    return movie


def sort_and_add_rank(movie_list):
    rank = 0
    previus_number_of_comments = 0
    for movie in movie_list:
        if movie['total_comments'] != previus_number_of_comments:
            rank += 1
            movie['rank'] = rank
        else:
            movie['rank'] = rank
        previus_number_of_comments = movie['total_comments']
    return movie_list
