from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.core import serializers
from book.models import Book
from borrow_flow.models import BorrowedBook
from datetime import datetime, timedelta
from borrow_flow.forms import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout

# Create your views here.
@login_required(login_url='/login')
def show_borrow_page(request, id):
    book = Book.objects.get(pk = id)
    context = {
        'user' : request.user.username,
        'book' : book,
        'book_id' : id
    }
    return render(request, "borrow.html", context)

@login_required(login_url='/login')
def show_yourbook_page(request):
    # borrowed_book = BorrowedBook.objects.filter(user = request.user)
    borrowed_book = BorrowedBook.objects.all()
    context = {
        'user' : request.user.username,
        # 'borrowed_book' : borrowed_book
        'borrowed_book' : borrowed_book
    }
    return render(request, 'yourbook.html', context)

@csrf_exempt
def borrow_book(request, id):
    if request.method == 'POST':
        terms_accepted_1 = request.POST.get('terms_accepted_1')
        terms_accepted_2 = request.POST.get('terms_accepted_2')
        terms_accepted_3 = request.POST.get('terms_accepted_3')

        if terms_accepted_1 and terms_accepted_2 and terms_accepted_3:
            book_to_be_borrowed = Book.objects.get(pk = id)
            borrow_duration = request.POST.get('borrow_duration')
            return_date = datetime.now() + timedelta(days=int(borrow_duration))
            borrowed_book = BorrowedBook(user=request.user, book=book_to_be_borrowed, borrow_duration=borrow_duration, return_date=return_date)
            borrowed_book.save()
            return redirect('borrow_flow:show_yourbook_page')
    return HttpResponseNotFound()
    
@csrf_exempt
def return_book(request, id):
    borrowed_book = BorrowedBook.objects.filter(user=request.user)
    for book in borrowed_book:
        if book.book.id == id:
            book.delete()
    return HttpResponse(b"RETURNED", status=201)

def get_book_by_id_json(request, id):
    book = Book.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('json', book), content_type="application/json")

def get_borrowed_book_json(request):
    borrowed_books = BorrowedBook.objects.filter(user=request.user)
    borrowed_books_data = []
    for borrowed_book in borrowed_books:
        book = {
            'id': borrowed_book.book.id,
            'book_authors': borrowed_book.book.book_authors,
            'book_desc': borrowed_book.book.book_desc,
            'book_edition': borrowed_book.book.book_edition,
            'book_format': borrowed_book.book.book_format,
            'book_isbn': borrowed_book.book.book_isbn,
            'book_pages': borrowed_book.book.book_pages,
            'book_rating': borrowed_book.book.book_rating,
            'book_rating_count': borrowed_book.book.book_rating_count,
            'book_review_count': borrowed_book.book.book_review_count,
            'book_title': borrowed_book.book.book_title,
            'genres': borrowed_book.book.genres,
            'image_url': borrowed_book.book.image_url,
        }
        data = {
            'user': borrowed_book.user.id,
            'book': book,
            'borrow_duration': borrowed_book.borrow_duration,
            'borrow_date': borrowed_book.borrow_date.strftime('%Y-%m-%d') if borrowed_book.borrow_date else None,
            'return_date': borrowed_book.return_date.strftime('%Y-%m-%d') if borrowed_book.return_date else None,
        }
        borrowed_books_data.append(data)
    return JsonResponse(borrowed_books_data, safe=False)

@csrf_exempt
def logout(request):
    username = request.user.username

    try:
        auth_logout(request)
        return JsonResponse({
            "username": username,
            "status": True,
            "message": "Logout berhasil!"
        }, status=200)
    except:
        return JsonResponse({
        "status": False,
        "message": "Logout gagal."
        }, status=401)
        

