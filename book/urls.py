from django.urls import path
from .views import get_json
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('api/books/', get_json, name='book-list'),
]