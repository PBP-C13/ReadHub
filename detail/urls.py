from django.urls import path
from .views import  *

app_name = 'detail'

urlpatterns = [
    path('detail/<int:id>/', show_detail, name='show_detail')
]