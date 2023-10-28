from django.urls import path
from category.views import show_category, get_product_json, add_book_favorit_ajax, show_favorit, get_book_favorit
from detail.views import show_detail

app_name = 'category'

urlpatterns = [
    path('', show_category, name='show_category'),
    path('detail/<int:id>/', show_detail, name='show_detail'),
    path('add_favorit/<int:book_id>/', add_book_favorit_ajax, name='book-list'),
    path('show-favorit', show_favorit, name='show_favorit'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('get-book-favorit/', get_book_favorit, name='get_book_favorit'),
]
