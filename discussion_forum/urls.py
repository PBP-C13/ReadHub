from django.urls import path
from .views import get_json
from .views import  *

app_name = 'forum'

urlpatterns = [
    path('', show_forum, name='show_forum'),
    path('create_forum/', create_forum, name='create_forum'),
    path('like_forum/', like_forum, name='like_forum'),
    path('unlike_forum/', unlike_forum, name='unlike_forum'),
    path('api/books/', get_json, name='book-list'), 
]