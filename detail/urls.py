from django.urls import path
from detail.views import show_detail, get_item_json, create_review_ajax, create_review
from borrow_flow.views import show_borrow_page

app_name = 'detail'

urlpatterns = [
    path('<int:id>/get-item-json/', get_item_json, name='get_item_json'),
    path('create_review_ajax/', create_review_ajax, name='create_review_ajax'),  
    path('create_review/', create_review, name='create_review'),  
    path('<int:id>/', show_detail, name='show_detail'),  
    path('<int:id>/', show_borrow_page, name='show_borrow_page'),
]
