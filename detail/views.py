from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.core import serializers
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from detail.forms import ReviewForm
from book.models import Book
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import random
from detail.models import Review

def show_detail(request, id):
    selected_book = Book.objects.get(pk=id)
    genres = selected_book.genres.split('|')[:3]
    selected_genres = random.sample(genres, 3)

    similar_books = Book.objects.filter(
        Q(genres__icontains=selected_genres[0]) | Q(genres__icontains=selected_genres[1]) | Q(genres__icontains=selected_genres[2])
    ).exclude(pk=id)[:6]

    book_reviews = Review.objects.filter(book=selected_book)

    context = {
        'book': selected_book,
        'user': request.user.username if request.user.is_authenticated else "Guest",
        'similar_books': similar_books,
        'genres': genres,
        'selected_genres': selected_genres,
        'reviews': book_reviews  # Add this line
    }
    return render(request, "detail.html", context)


def get_item_json(request, id):
    product_items = []
    # Filter reviews by book id
    reviews = Review.objects.filter(book_id=id)
    
    for r in reviews:
        product_item = {
            'user': r.user.username if r.user else "Guest",
            'review': r.review
        }
        product_items.append(product_item)

    return JsonResponse(product_items, safe=False)


@login_required(login_url='/login')
def create_review(request):
    if request.method == "POST":
        rev = ReviewForm(request.POST)
        if rev.is_valid():
            r = rev.save(commit=False)
            r.user = request.user  
            r.save()
            return HttpResponseRedirect(reverse('detail:show_detail'))
        else:
            print(rev.errors)
    else:
        rev = ReviewForm()

    context = {'rev': rev}
    return render(request, "create_detail.html", context)
    
@login_required
@csrf_exempt
def create_review_ajax(request):
    if request.method == 'POST':
        review_text = request.POST.get("book_review")
        book_id = request.POST.get("book_id")  
        book = Book.objects.get(pk=book_id)
        newReview = Review(user=request.user, review=review_text, book=book)
        newReview.save()
        
    return HttpResponse(b"CREATED", status=201)
