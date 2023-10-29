from django.urls import path
from detail.views import show_detail, get_item_json, create_review

app_name = 'detail'

urlpatterns = [
    path('get-item-json/', get_item_json, name='get_item_json'),
    path('create_review/', create_review, name='create_review'),  # This line is sufficient.
    path('detail/<int:id>/', show_detail, name='show_detail'),  # Remove this redundant line.
]
