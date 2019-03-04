from django.shortcuts import render, get_object_or_404

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
# Create your views here.

from .serializers import MovieSerializer
from .services import fetch_movie_data
from .models import Movie


class MovieViewSet(APIView):
    def post(self, request, *args, **kwargs):
        movie_data = fetch_movie_data(request.data['title'])
        if movie_data['Response'] == 'False':
            return Response(movie_data, status=status.HTTP_400_BAD_REQUEST)
        if get_object_or_404(Movie, imdbID=movie_data['imdbID']):
            return Response({'Error': "This movie already exist in Database"},
                            status=status.HTTP_400_BAD_REQUEST)
        movie_serializer = MovieSerializer(data=movie_data)
        if movie_serializer.is_valid():
            movie_serializer.save()
            return Response(movie_serializer.data, status=status.HTTP_201_CREATED)
        return Response(movie_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        return Response(MovieSerializer(Movie.objects.all(), many=True).data, status=status.HTTP_200_OK)
