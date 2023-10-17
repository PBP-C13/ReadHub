from django.urls import path
from category.views import show_category

app_name = 'category'

urlpatterns = [
    path('', show_category, name='show_category'),
]