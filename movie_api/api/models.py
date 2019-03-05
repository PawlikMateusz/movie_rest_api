from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.


class Rating(models.Model):
    Movie = models.ForeignKey(
        'Movie', on_delete=models.CASCADE, related_name='Ratings')
    Source = models.CharField(max_length=100)
    Value = models.CharField(max_length=10)


class Movie(models.Model):
    Title = models.CharField(max_length=200)
    Year = models.CharField(max_length=10, null=True, blank=True)
    Rated = models.CharField(max_length=20, null=True, blank=True)
    Released = models.CharField(max_length=50, null=True, blank=True)
    Runtime = models.CharField(max_length=10, null=True, blank=True)
    Genre = models.CharField(max_length=100, null=True, blank=True)
    Director = models.CharField(max_length=100, null=True, blank=True)
    Writer = models.CharField(max_length=500, null=True, blank=True)
    Actors = models.CharField(max_length=200, null=True, blank=True)
    Plot = models.TextField(null=True, blank=True)
    Language = models.CharField(max_length=100, null=True, blank=True)
    Country = models.CharField(max_length=100, null=True, blank=True)
    Awards = models.CharField(max_length=200, null=True, blank=True)
    Poster = models.CharField(max_length=300, null=True, blank=True)
    Metascore = models.CharField(max_length=50, null=True, blank=True)
    imdbRating = models.CharField(max_length=50, null=True, blank=True)
    imdbVotes = models.CharField(max_length=30, null=True, blank=True)
    imdbID = models.CharField(max_length=100)
    Type = models.CharField(max_length=50, null=True, blank=True)
    DVD = models.CharField(max_length=50, null=True, blank=True)
    BoxOffice = models.CharField(max_length=100, null=True, blank=True)
    Production = models.CharField(max_length=50, null=True, blank=True)
    Website = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.Title


class Comment(models.Model):
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name='comments')
    text = models.CharField(max_length=300)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.text
