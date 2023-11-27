from django.urls import path
from borrow_flow.views import * 

app_name = 'borrow_flow'

urlpatterns = [
    path('<int:id>/', show_borrow_page, name='show_borrow_page'),
    path('borrow_book/<int:id>/', borrow_book, name='borrow_book'),
    path('return_book/<int:id>/', return_book, name='return_book'),
    path('get_borrowed_book_json', get_borrowed_book_json, name='get_borrowed_book_json'),
    path('get_book_by_id_json/<int:id>/', get_book_by_id_json, name='get_book_by_id_json'),
    path('show_yourbook_page/', show_yourbook_page, name='show_yourbook_page'),
    path('logout/', logout, name='logout'),
]


