from django.urls import path, include
from rest_framework import routers

from .views import MovieViewSet, CommentViewSet, TopMoviesView

app_name = "api"

router = routers.SimpleRouter()
router.register('comments', CommentViewSet)
router.register('movies', MovieViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('top/', TopMoviesView.as_view(), name='top_movies')
]
