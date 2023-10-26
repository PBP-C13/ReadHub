from django.urls import path
from .views import get_json
from .views import  *

app_name = 'forum'

urlpatterns = [
    path('', show_forum, name='show_forum'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create_forum/', create_forum, name='create_forum'),
    path('like_forum/', like_forum, name='like_forum'),
    path('unlike_forum/', unlike_forum, name='unlike_forum'),
    path('remove_forum_ajax/<int:id>', remove_forum_ajax , name='remove_forum_ajax'),
    path('api/books/', get_json, name='book-list'), 
]