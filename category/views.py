from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import render
from django.forms import ModelForm
from category.models import Category
from book.models import Book
from django.http import HttpResponseRedirect
from category.forms import FavoritForm
from django.urls import reverse
from django.core import serializers
import favorit

# Create your views here.
def show_category(request):
    categories = Category.objects.all()
    # Ambil semua buku dalam basis data
    all_books = Book.objects.all()[:100]
    fantasy_books = Book.objects.filter(genres__icontains="fantasy")[:15]

    context = {
        'name': request.user.username,
        'categories': categories,
        'books': all_books,
        'fantasyBooks':fantasy_books,
    }

    return render(request, "category.html", context)

def add_books_to_category(request):
    category = Category.objects.get(name_category='Fiksi')  # Ganti 'Fiksi' dengan nama kategori yang sesuai
    books_to_add = Book.objects.filter(genre='Fiksi')  

    for book in books_to_add:
        category.books.add(book)

    return HttpResponse("Buku-buku telah ditambahkan ke kategori Fiksi.")

#fungsi untuk mengembalikan data jason:
def get_product_json(request):
    all_books = Book.objects.all()[:100]
    return HttpResponse(serializers.serialize('json', all_books))
