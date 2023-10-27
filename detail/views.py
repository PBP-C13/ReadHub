from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from detail.forms import DetailForm
from detail.models import Detail
from book.models import Book
import random

def show_detail(request, id):
    detail = Detail.objects.get(pk=id)
    all_books = Book.objects.get(pk=id)
    genres = all_books.genres.split('|')[:3]

    # Create a queryset for similar books
    similar_books = Book.objects.filter(genres__icontains=genres[0])
    for genre in genres[1:]:
        similar_books = similar_books.filter(genres__icontains=genre)
    
    context = {
        'detail': detail,  
        'book': all_books,
        'name': request.user.username if request.user.is_authenticated else "Guest",
        'similar_books': similar_books,  # Pass similar_books to the template
        'genres': genres
    }
    return render(request, "detail.html", context)

def borrow_flow(request):
    # Add view logic for the borrow flow here
    return render(request, 'borrow_flow.html')

def get_item_json(request):
    all_books = Book.objects.all()
    return HttpResponse(serializers.serialize('json', all_books))

@csrf_exempt
def create_review(request):
    if request.method == "POST":
        book_review = request.POST.get("book_review")
        newReview = Detail(book_review=book_review)
        newReview.save()

        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()