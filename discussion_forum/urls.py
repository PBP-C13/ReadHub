from django.urls import path
from .views import get_json
from .views import show_forum

app_name = 'favorit'

urlpatterns = [
    path('', show_forum, name='show_forum'),
    path('api/books/', get_json, name='book-list'),
]