from django.shortcuts import render
from django.db.models import Count

from django_filters import rest_framework as filters
from rest_framework.views import APIView
from rest_framework import status, mixins, viewsets, generics
from rest_framework.response import Response
# Create your views here.

from .serializers import MovieSerializer, CommentSerializer
from .services import (
    fetch_and_validate_movie,
    sort_and_add_rank,
)
from .models import Movie, Comment


class MovieViewSet(APIView):
    def post(self, request, *args, **kwargs):
        if not 'title' in request.data:
            return Response({'Error': "Please add title param :)"}, status=status.HTTP_400_BAD_REQUEST)
        movie_data = fetch_and_validate_movie(request.data['title'])
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
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        if start_date > end_date:
            return Response({'Error': "You provided wrong date range! Start date is bigger than end date"},
                            status=status.HTTP_400_BAD_REQUEST)
        movie_list = self.filter_queryset(self.queryset)
        movie_list = movie_list.values(
            'movie_id').annotate(total_comments=Count('movie')).order_by('-total_comments')
        movie_list = sort_and_add_rank(movie_list)
        return Response(movie_list, status=status.HTTP_200_OK)
