from django.urls import path
from main.views import show_main
from main.views import * 


app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('get-privacy-policy/', get_privacy_policy, name='get_privacy_policy'),
    path('privacy_policy/', privacy_policy, name='privacy_policy'),
]