from django.urls import path
from borrow_flow.views import * 

app_name = 'borrow_flow'

urlpatterns = [
    path('', show_borrow_page, name='show_borrow_page'),
    path('borrow_book/<int:id>/', borrow_book, name='borrow_book'),
    path('return_book/<int:id>/', return_book, name='return_book')
]


