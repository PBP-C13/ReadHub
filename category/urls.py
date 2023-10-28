from django.urls import path
from category.views import show_category, get_product_json
from detail.views import show_detail
from favorit.views import add_book_favorit_ajax

app_name = 'category'

urlpatterns = [
    path('', show_category, name='show_category'),
    path('detail/<int:id>/', show_detail, name='show_detail'),
    path('favorit/api/books/<int:book_id>/', add_book_favorit_ajax, name='book-list'),
    path('get-product/', get_product_json, name='get_product_json'),
]
