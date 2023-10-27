from django.urls import path
from category.views import show_category
from detail.views import show_detail

app_name = 'category'

urlpatterns = [
    path('', show_category, name='show_category'),
    path('detail/<int:id>/', show_detail, name='show_detail'),
]
