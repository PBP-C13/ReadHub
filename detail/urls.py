from django.urls import path
from .views import  *

app_name = 'detail'

urlpatterns = [
    path('<int:id>/', show_detail, name='show_detail')
]