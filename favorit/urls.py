from django.urls import path
from .views import show_favorit, get_book_json, add_book_favorit_ajax
from category.views import show_category

app_name = 'favorit'

urlpatterns = [
    path('', show_favorit, name='show_favorit'),
    path('get-product/', get_book_json, name='get_book_json'),
    path('category/favorit/api/books/<int:book_id>/', add_book_favorit_ajax, name='book-list'),
    path('category/', show_category, name='category'),
]