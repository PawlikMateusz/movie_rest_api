from rest_framework import serializers

from .models import Movie, Comment


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('__all__')


class CommentSerializer(serializers.ModelSerializer):
    movie_id = serializers.PrimaryKeyRelatedField(
        queryset=Movie.objects.all(), source='movie')

    class Meta:
        model = Comment
        fields = ('movie_id', 'text')
