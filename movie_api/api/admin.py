from django.contrib import admin

# Register your models here.
from .models import Movie, Comment

admin.site.register(Movie)
admin.site.register(Comment)
