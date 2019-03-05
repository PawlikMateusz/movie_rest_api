import os
import requests
from django.http import request
from rest_framework.response import Response
from rest_framework import status

from .models import Movie


API_KEY = os.getenv("API_KEY", None)


def fetch_and_validate_movie(title):
    url = 'http://www.omdbapi.com/?t={0}&apikey={1}'.format(title, API_KEY)
    response = requests.get(url)
    if response.ok:
        movie = response.json()
        if movie['Response'] == 'False':
            return Response(movie, status=status.HTTP_400_BAD_REQUEST)
        if Movie.objects.filter(imdbID=movie['imdbID']):
            return Response({'Error': "This movie already exist in Database"},
                            status=status.HTTP_400_BAD_REQUEST)
        return movie
    return Response({'Error': "There is something wrong with external API"},
                    status=status.HTTP_400_BAD_REQUEST)


def add_rank_field(movie_list):
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
