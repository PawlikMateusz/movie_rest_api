from django.test import TestCase
from .factories import MovieFactory, CommentFactory
import pytest


class TestMovieModel(TestCase):
    @pytest.mark.django_db
    def test_movie_model(self):
        movie = MovieFactory()
        assert movie.__str__() == movie.Title


class TestCommentModel(TestCase):
    @pytest.mark.django_db
    def test_comment_model(self):
        comment = CommentFactory()
        assert comment.__str__() == comment.text
