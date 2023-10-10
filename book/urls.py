from django.urls import path
from main.views import show_main
from .api import BookListView



app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('api/books/', BookListView.as_view(), name='book-list'),
    
]