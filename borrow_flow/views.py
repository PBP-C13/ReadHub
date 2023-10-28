from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.core import serializers
from borrow_flow.models import Book, BorrowedBook
from datetime import datetime, timedelta
from borrow_flow.forms import *
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def show_borrow_page(request, id):
    book = Book.objects.get(pk = id)
    context = {
        'user' : request.user.username,
        'book' : book
    }
    return render(request, "borrow.html", context)

@csrf_exempt
def borrow_book(request, id):
    if request.method == 'POST' and request.POST.get('terms_accepted'):
        book = get_object_or_404(Book, pk=id)
        user = request.user
        borrow_duration = request.POST.get('borrow_duration')
        return_date = datetime.now() + timedelta(days=borrow_duration)
        borrowed_book = BorrowedBook(user=user, book=book, borrow_duration=borrow_duration, return_date=return_date)
        borrowed_book.save()
        return HttpResponse(b"BORROWED", status=201)
    return HttpResponseNotFound()
        
@csrf_exempt
def return_book(request, id):
    borrowed_book = get_object_or_404(BorrowedBook, pk=id)
    borrowed_book.delete()
    return HttpResponse(b"RETURNED", status=201)

def get_borrowed_book_json(request):
    borrowed_books = BorrowedBook.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', borrowed_books))

