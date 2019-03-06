from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIRequestFactory
from rest_framework import status
from rest_framework.response import Response

from unittest.mock import Mock, patch
import pytest

from .factories import MovieFactory, CommentFactory
from api.views import MovieViewSet, TopMoviesView


@patch('api.services.requests.get')
class TestMovieModel(TestCase):
    def setUp(self):
        self.movie = {
            "Title": "Shallow",
            "Year": "2012",
            "Rated": "N/A",
            "Released": "20 Jun 2013",
            "Runtime": "16 min",
            "Genre": "Short, Drama, Thriller",
            "Ratings": [
                {
                    "Source": "Internet Movie Database",
                    "Value": "8.0/10"
                }
            ],
            "Metascore": "N/A",
            "imdbRating": "8.0",
            "imdbVotes": "62",
            "imdbID": "tt2203808",
            "Response": "True"
        }
        self.movie_not_found = {
            "Response": "False"
        }
        self.movie_without_title_field = {
            "imdbID": "tt2203808",
            "Response": "True"
        }
        self.movie_not_found_response = Response(
            self.movie_not_found, status=status.HTTP_400_BAD_REQUEST)
        self.get_movies = MovieViewSet.as_view(
            actions={'get': 'retrieve'})
        self.post_movie = MovieViewSet.as_view(
            actions={'post': 'create'})
        self.request_factory = APIRequestFactory()

    def test_status_code(self, mock_get):
        request = self.request_factory.get(
            '/api/movies')
        response = self.get_movies(request)
        assert response.status_code == status.HTTP_200_OK

    def test_object_creation(self, mock_get):
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = self.movie
        request = self.request_factory.post(
            '/api/movies/',  {'title': 'new idea'}, format='json')
        response = self.post_movie(request)
        assert response.status_code == status.HTTP_201_CREATED

    def test_movie_not_found(self, mock_get):
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = self.movie_not_found
        request = self.request_factory.post(
            '/api/movies/',  {'title': 'new idea'}, format='json')
        response = self.post_movie(request)
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_no_title_in_post_request(self, mock_get):
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = self.movie_not_found
        request = self.request_factory.post(
            '/api/movies/', format='json')
        response = self.post_movie(request)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data == {'Error': "Please add title param :)"}

    def test_invalid_serializer(self, mock_get):
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = self.movie_without_title_field
        request = self.request_factory.post(
            '/api/movies/', {'title': 'new idea'}, format='json')
        response = self.post_movie(request)
        assert response.status_code == status.HTTP_400_BAD_REQUEST


class TestTopMoviesViewSet(TestCase):
    @pytest.mark.django_db
    def setUp(self):
        movie = MovieFactory()
        movie2 = MovieFactory()
        movie3 = MovieFactory()
        movie4 = MovieFactory()
        comment_1 = CommentFactory(movie=movie)
        comment_2 = CommentFactory(movie=movie)
        comment_3 = CommentFactory(movie=movie2)
        comment_4 = CommentFactory(movie=movie3)
        self.get_top_movies = TopMoviesView.as_view()
        self.request_factory = APIRequestFactory()

    def test__response_status_code(self):
        request = self.request_factory.get('/api/top/')
        response = self.get_top_movies(request)
        assert response.status_code == status.HTTP_200_OK

    def test_wrong_date_range(self):
        request = self.request_factory.get(
            '/api/top/?start_date=2019-03-01&end_date=2019-02-01')
        response = self.get_top_movies(request)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data == {
            'Error': "You provided wrong date range! Start date is bigger than end date"}
