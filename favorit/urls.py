from django.urls import path
from .views import get_json
from .views import show_favorit 

app_name = 'favorit'

urlpatterns = [
    path('', show_favorit, name='show_favorit'),
    path('api/books/', get_json, name='book-list'),
]