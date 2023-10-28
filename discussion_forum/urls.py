from django.urls import path
from .views import get_json
from .views import  *

app_name = 'forum'

urlpatterns = [
    path('', show_forum, name='show_forum'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create_forum/', create_forum, name='create_forum'),
    path('delete_item/<int:item_id>/', delete_item, name='delete_item'),
    path('api/books/', get_json, name='book-list'), 
    path('toggle-like/<int:id>/', toggle_like_forum, name='toggle-like'),
    path('like/<int:post_id>/', like_forum_post, name='like_forum_post'),
]