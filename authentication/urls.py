from django.urls import path
from authentication.views import login
from authentication.views import logout
from authentication.views import register


app_name = 'authentication'

urlpatterns = [
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('login/', login, name='login'),
]