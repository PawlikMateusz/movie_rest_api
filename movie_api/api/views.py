from django.shortcuts import render
from django.db.models import Count

from django_filters import rest_framework as filters
from rest_framework import filters as rest_filters
from rest_framework.views import APIView
from rest_framework import status, mixins, viewsets, generics
from rest_framework.response import Response
# Create your views here.

from .serializers import MovieSerializer, CommentSerializer
from .services import (
    fetch_and_validate_movie,
    add_rank_field,
)
from .models import Movie, Comment


class MovieViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = (rest_filters.SearchFilter, rest_filters.OrderingFilter,)
    search_fields = ('Actors', 'Genre')
    ordering_fields = ('imdbRating',)

    def post(self, request, *args, **kwargs):
        if not 'title' in request.data:
            return Response({'Error': "Please add title param :)"}, status=status.HTTP_400_BAD_REQUEST)
        movie_data = fetch_and_validate_movie(request.data['title'])
        if type(movie_data) is Response:
            return movie_data
        movie_serializer = MovieSerializer(data=movie_data)
        if movie_serializer.is_valid():
            movie_serializer.save()
            return Response(movie_serializer.data, status=status.HTTP_201_CREATED)
        return Response(movie_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        return Response(MovieSerializer(Movie.objects.all(), many=True).data, status=status.HTTP_200_OK)


class CommentViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ("movie_id",)


class TopMoviesFilter(filters.FilterSet):
    start_date = filters.DateFilter(field_name="created_at", lookup_expr='gte')
    end_date = filters.DateFilter(field_name="created_at", lookup_expr=('lte'))

    class Meta:
        model = Comment
        fields = ['start_date', 'end_date']


class TopMoviesView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TopMoviesFilter

    def list(self, request, *args, **kwargs):
        start_date = self.request.GET.get('start_date', None)
        end_date = self.request.GET.get('end_date', None)
        if (start_date and end_date) and (start_date > end_date):
            return Response({'Error': "You provided wrong date range! Start date is bigger than end date"},
                            status=status.HTTP_400_BAD_REQUEST)
        movie_list = self.filter_queryset(self.queryset)
        movie_list = movie_list.values(
            'movie_id').annotate(total_comments=Count('movie')).order_by('-total_comments')
        movie_list = add_rank_field(movie_list)
        return Response(movie_list, status=status.HTTP_200_OK)
