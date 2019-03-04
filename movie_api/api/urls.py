from django.urls import path, include
from rest_framework import routers

from .views import MovieViewSet

app_name = "api"

router = routers.DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path('movies/', MovieViewSet.as_view(), name='movies_endpoint')
]
