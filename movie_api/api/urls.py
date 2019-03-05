from django.urls import path, include
from rest_framework import routers

from .views import MovieViewSet, CommentViewSet, TopMoviesView

app_name = "api"

router = routers.SimpleRouter()
router.register('comments', CommentViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('movies/', MovieViewSet.as_view(), name='movies'),
    path('top/', TopMoviesView.as_view(), name='top_movies')
]
