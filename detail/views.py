from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from .forms import ReviewForm
from detail.models import Detail
from book.models import Book
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import random

def show_detail(request, id):
    detail = Book.objects.get(pk=id)
    selected_book = Book.objects.get(pk=id)
    genres = selected_book.genres.split('|')[:3]
    selected_genres = random.sample(genres, 3)
    # Create a queryset for similar books
    similar_books = Book.objects.filter(
    Q(genres__icontains=selected_genres[0]) | Q(genres__icontains=selected_genres[1]) | Q(genres__icontains=selected_genres[2])
    ).exclude(pk=id)[:6]

    context = {
        'detail': detail,
        'book': selected_book,
        'name': request.user.username if request.user.is_authenticated else "Guest",
        'similar_books': similar_books,
        'genres': genres,
        'selected_genres' : selected_genres,
        'book_id' : id 
        
    }
    return render(request, "detail.html", context)


# Rest of your code remains the same.

def borrow_flow(request):
    # Add view logic for the borrow flow here
    return render(request, 'borrow_flow.html')

def get_item_json(request):
    all_books = Book.objects.all()
    return HttpResponse(serializers.serialize('json', all_books))

@login_required
@csrf_exempt
def create_review(request):
    if request.method == "POST":
        book_review = request.POST.get("book_review")
        name = request.POST.get("name")

        # Create a new review associated with the book
        newReview = Detail(name=name, book_review=book_review)
        newReview.save()

        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()
