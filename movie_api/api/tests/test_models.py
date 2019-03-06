from django.test import TestCase

import pytest

from .factories import MovieFactory, CommentFactory


class TestMovieModel(TestCase):
    @pytest.mark.django_db
    def test_movie_string_represenation(self):
        movie = MovieFactory()
        assert movie.__str__() == movie.Title


class TestCommentModel(TestCase):
    @pytest.mark.django_db
    def test_comment_string_represenation(self):
        comment = CommentFactory()
        assert comment.__str__() == comment.text
