from django.urls import path
from .views import get_json
from .views import show_book


app_name = 'book'

urlpatterns = [
    path('', show_book, name='show_book'),
    path('api/books/', get_json, name='book-list'),
]