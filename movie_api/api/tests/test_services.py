from django.test import TestCase
from rest_framework import status
from unittest.mock import Mock, patch
import pytest

from .factories import MovieFactory
from api.services import fetch_and_validate_movie, add_rank_field


@patch('api.services.requests.get')
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
        self.movie_not_found = {
            "Response": "False"
        }

    def test_if_response_is_valid(self, mock_get):
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = self.movie
        response = fetch_and_validate_movie('Shallow')
        assert response == self.movie

    def test_if_response_is_dict(self, mock_get):
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = self.movie
        response = fetch_and_validate_movie('Shallow')
        assert type(response) == dict

    def test_if_movie_is_not_found(self, mock_get):
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = self.movie_not_found
        response = fetch_and_validate_movie('Shallow')
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    @pytest.mark.django_db
    def test_if_movie_already_exist_in_app_db(self, mock_get):
        movie_in_app_db = MovieFactory(
            Title="Shallow", imdbID='tt2203808')
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = self.movie
        response = fetch_and_validate_movie('Shallow')
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_if_there_is_problem_with_api(self, mock_get):
        mock_get.return_value = Mock(ok=False)
        mock_get.return_value.json.return_value = self.movie
        response = fetch_and_validate_movie('Shallow')
        assert response.status_code == status.HTTP_400_BAD_REQUEST


class TestAddRank(TestCase):
    def setUp(self):
        self.movie_list = [
            {
                "movie_id": 3,
                "total_comments": 5,
            },
            {
                "movie_id": 1,
                "total_comments": 4,
            },
            {
                "movie_id": 2,
                "total_comments": 4,
            },
            {
                "movie_id": 4,
                "total_comments": 3,
            }
        ]

    def test_if_there_is_added_rank_to_dict(self):
        ranked_list = add_rank_field(self.movie_list)
        assert next(iter(ranked_list))['rank']

    def test_rank_for_the_same_number_of_comments(self):
        ranked_list = add_rank_field(self.movie_list)
        assert ranked_list[2]['rank'] == ranked_list[1]['rank']

    def test_if_repsonse_is_list(self):
        ranked_list = add_rank_field(self.movie_list)
        assert type(ranked_list) == list
