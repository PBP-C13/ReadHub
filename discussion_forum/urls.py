from django.urls import path
from .views import get_json
from .views import  *

app_name = 'forum'

urlpatterns = [
    path('', show_forum, name='show_forum'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('get-product-filter/<str:genre>/', get_product_json_filter, name='get_product_json'),
    path('create_forum/', create_forum, name='create_forum'),
    path('delete_item/<int:item_id>/', delete_item, name='delete_item'),
    path('like_forum/', like_forum, name='like_forum'),
    path('unlike_forum/', unlike_forum, name='unlike_forum'),
    path('remove_forum_ajax/<int:id>', remove_forum_ajax , name='remove_forum_ajax'),
    path('api/books/', get_json, name='book-list'), 
]