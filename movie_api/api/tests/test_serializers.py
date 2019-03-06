from django.test import TestCase
from django.shortcuts import get_object_or_404

import pytest

from api.serializers import MovieSerializer
from api.models import Rating, Movie


@pytest.mark.django_db
class TestFetchData(TestCase):
    def setUp(self):
        self.movie = {
            "Title": "Shallow",
            "Year": "2012",
            "Rated": "N/A",
            "Released": "20 Jun 2013",
            "Runtime": "16 min",
            "Genre": "Short, Drama, Thriller",
            "Director": "William Bridges",
            "Writer": "William Bridges",
            "Actors": "Amelia Beney, Emily Bruni, Dan Stevens",
            "Plot": "When newly elected MP Richard Dove runs over a young girl on a deserted forest road he fatally decides to bury her in the woods and save his blossoming career. But when he returns to his ...",
            "Language": "English",
            "Country": "UK",
            "Awards": "N/A",
            "Poster": "https://images-na.ssl-images-amazon.com/images/M/MV5BMTQ3ODE1MjU3N15BMl5BanBnXkFtZTgwMDM1MzMxNzE@._V1_SX300.jpg",
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
            "Type": "movie",
            "DVD": "N/A",
            "BoxOffice": "N/A",
            "Production": "N/A",
            "Website": "N/A",
            "Response": "True"
        }
        self.serializer = MovieSerializer(data=self.movie)

    def test_contains_required_fields(self):
        self.serializer.is_valid()
        data = self.serializer.data
        assert data['imdbID']
        assert data['Title']

    def test_if_objects_are_created(self):
        self.serializer.is_valid()
        movie = self.serializer.save()
        rating = get_object_or_404(Rating, Movie=movie)
        assert type(rating) == Rating
        assert type(movie) == Movie

    def test_if_serializers_returns_correct_data(self):
        self.serializer.is_valid()
        data = self.serializer.data
        assert data['imdbID'] == self.movie['imdbID']
        assert data['Title'] == self.movie['Title']
