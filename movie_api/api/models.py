from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.


class Rating(models.Model):
    Movie = models.ForeignKey(
        'Movie', on_delete=models.CASCADE, related_name='ratings')
    Source = models.CharField(max_length=100)
    Value = models.CharField(max_length=10)


class Movie(models.Model):
    Title = models.CharField(max_length=200)
    Year = models.PositiveIntegerField()
    Rated = models.CharField(max_length=20)
    Released = models.CharField(max_length=50)
    Runtime = models.CharField(max_length=10)
    Genre = models.CharField(max_length=100)
    Director = models.CharField(max_length=100)
    Writer = models.CharField(max_length=300)
    Actors = models.CharField(max_length=200)
    Plot = models.TextField()
    Language = models.CharField(max_length=100)
    Country = models.CharField(max_length=20)
    Awards = models.CharField(max_length=200)
    Poster = models.CharField(max_length=300)
    Metascore = models.CharField(max_length=30)
    imdbRating = models.DecimalField(max_digits=2, decimal_places=1)
    imdbVotes = models.CharField(max_length=30)
    imdbID = models.CharField(max_length=100)
    Type = models.CharField(max_length=30)
    DVD = models.CharField(max_length=30)
    BoxOffice = models.CharField(max_length=100)
    Production = models.CharField(max_length=50)
    Website = models.CharField(max_length=300)
