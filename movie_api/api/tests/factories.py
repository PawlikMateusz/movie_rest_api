import factory
from random import randint
from faker import Factory
from django.apps import apps

Movie = apps.get_model('api.Movie')
Rating = apps.get_model('api.Rating')
Comment = apps.get_model('api.Comment')


faker = Factory.create()


class MovieFactory(factory.DjangoModelFactory):
    class Meta:
        model = Movie

    Title = faker.name()
    imdbID = randint(0, 100000)


class CommentFactory(factory.DjangoModelFactory):
    class Meta:
        model = Comment

    movie = factory.SubFactory(MovieFactory)
    text = faker.text()
