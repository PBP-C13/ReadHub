from django.urls import path
from detail.views import show_detail, borrow_flow, get_item_json, create_review

app_name = 'detail'

urlpatterns = [
    path('borrow_flow/', borrow_flow, name='borrow_flow'),
    path('get-item-json/', get_item_json, name='get_item_json'),
    path('create-review/', create_review, name='create_review'),
    path('detail/<int:id>/', show_detail, name='show_detail'),
    
]