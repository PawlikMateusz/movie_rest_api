from rest_framework import serializers

from .models import Movie, Comment, Rating


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('Source', 'Value')
        read_only_fields = ('Movie',)


class MovieSerializer(serializers.ModelSerializer):
    Ratings = RatingSerializer(many=True)

    class Meta:
        model = Movie
        fields = ('__all__')

    def create(self, validated_data):
        ratings = validated_data.pop('Ratings')
        movie = Movie.objects.create(**validated_data)
        for rating in ratings:
            rating = Rating.objects.create(Movie=movie, **rating)
        return movie


class CommentSerializer(serializers.ModelSerializer):
    movie_id = serializers.PrimaryKeyRelatedField(
        queryset=Movie.objects.all(), source='movie')

    class Meta:
        model = Comment
        fields = ('movie_id', 'text')
