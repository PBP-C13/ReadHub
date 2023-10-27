from django.shortcuts import redirect, render
from borrow_flow.models import Book, BorrowedBook
from datetime import datetime, timedelta
from borrow_flow.forms import *

# Create your views here.
def show_borrow_page(request, id):
    book = Book.objects.get(pk = id)
    context = {
        'user' : request.user.username,
        'book' : book
    }
    return render(request, "borrow.html", context)

def borrow_book(request, id):
    book = Book.objects.get(pk=id)
    if request.method == 'POST':
        form = BorrowForm(request.POST)
        if form.is_valid() and form.cleaned_data['terms_accepted']:
            borrowed_book = form.save(commit=False)
            borrowed_book.book = book
            borrowed_book.user = request.user
            borrowed_book.borrow_duration = form.cleaned_data['borrow_duration']
            borrowed_book.return_date = datetime.now() + timedelta(days=borrowed_book.borrow_duration)
            borrowed_book.save()
            return redirect()
    
    context = {
        'form' : form, 
        'book' : book
    }
    return render(request, 'borrow.html', context)

def return_book(request, id):
    return

