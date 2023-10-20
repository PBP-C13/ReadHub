from django.http import HttpResponse
from django.shortcuts import render
from django.forms import ModelForm
from category.models import Category
from book.models import Book
import random

# Create your views here.
def show_category(request):
    categories = Category.objects.all()
    # Ambil semua buku dalam basis data
    all_books = Book.objects.all()

    # Acak urutan buku
    random_books = random.sample(list(all_books), 300)  #agar memilih 300 buku random dari database
    context = {
        'categories': categories,
        'books': random_books
    }

    return render(request, "category.html", context)

def add_books_to_category(request):
    category = Category.objects.get(name_category='Fiksi')  # Ganti 'Fiksi' dengan nama kategori yang sesuai
    books_to_add = Book.objects.filter(genre='Fiksi')  # Ganti 'Fiksi' dengan genre yang sesuai

    for book in books_to_add:
        category.books.add(book)

    return HttpResponse("Buku-buku telah ditambahkan ke kategori Fiksi.")
