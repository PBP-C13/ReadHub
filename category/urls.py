from django.urls import path
from category.views import show_category, get_product_json, add_book_favorit_ajax, show_favorit, get_book_favorit, delete_favorit, show_json_favorit
from detail.views import create_review_flutter, get_item_json, get_item_json_flutter, show_detail

app_name = 'category'

urlpatterns = [
    path('', show_category, name='show_category'),
    path('detail/<int:id>/', show_detail, name='show_detail'),
    path('add_favorit/<int:book_id>/', add_book_favorit_ajax, name='book-list'),
    path('delete_favorit/<int:book_id>/', delete_favorit, name='delete_book'),   
    path('show-favorit', show_favorit, name='show_favorit'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('get-book-favorit/', get_book_favorit, name='get_book_favorit'),
    path('json/', show_json_favorit, name='show_json'), 
    path('detail/<int:id>/get-item-json/', get_item_json, name='get_item_json'),
    path('detail/<int:id>/create_review_flutter', create_review_flutter, name='create_review_flutter'),
    path('detail/<int:id>/get-item-json-flutter/', get_item_json_flutter, name='get_item_json_flutter'),
]
