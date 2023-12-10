from django.urls import path
from detail.views import show_detail, get_item_json, create_review_ajax, create_review, create_review_flutter, get_item_json_flutter
from borrow_flow.views import show_borrow_page

app_name = 'detail'

urlpatterns = [
    path('<int:id>/get-item-json/', get_item_json, name='get_item_json'),
    path('create_review_ajax/', create_review_ajax, name='create_review_ajax'),  
    path('create_review/', create_review, name='create_review'),  
    path('<int:id>/', show_detail, name='show_detail'),  
    path('<int:id>/', show_borrow_page, name='show_borrow_page'),
    path('<int:id>/create_review_flutter/', create_review_flutter, name='create_review_flutter'),
    path('<int:id>/get-item-json-flutter/', get_item_json_flutter, name='get_item_json_flutter'),

]
