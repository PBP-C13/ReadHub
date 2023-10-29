from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import render
from django.forms import ModelForm
from category.models import Category
from book.models import Book
from django.http import HttpResponseRedirect
from category.forms import FavoritForm
from django.urls import reverse
from django.core import serializers
from django.contrib.auth.decorators import login_required
import favorit

# Create your views here.
def show_category(request):
    categories = Category.objects.all().values("books")
    # Ambil semua buku dalam basis data
    all_books = Book.objects.all()
    fantasy_books = Book.objects.filter(genres__icontains="fantasy")
    mystery_books = Book.objects.filter(genres__icontains="mystery")
    romance_books = Book.objects.filter(genres__icontains="romance")
    nonfiction_books = Book.objects.filter(genres__icontains="nonfiction")
    sciencefiction_books = Book.objects.filter(genres__icontains="science fiction")

    context = {
        'name': request.user.username,
        'categories': categories,
        'books': all_books,
        'fantasyBooks':fantasy_books,
        'mysteryBooks':mystery_books,
        'romanceBooks':romance_books,
        'nonfictionBooks': nonfiction_books,
        'sciencefictionBooks': sciencefiction_books,
    }

    return render(request, "category.html", context)

@login_required(login_url='/login')
def show_favorit(request):
    categories = Category.objects.all()
    # Ambil semua buku dalam basis data

    context = {
        'name': request.user.username,
        'categories': categories,
    }

    return render(request, "favoritpage.html", context)

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

def get_book_favorit(request):
    product_items = []
    favorit_books = Category.objects.all()
    for favorit in favorit_books:
        book = Book.objects.get(id=favorit.books.pk)  
        # Buat dictionary baru dengan data forum dan buku
        product_item = {
            'book_image':book.image_url,
            'book_title': book.book_title,
            'book_author': book.book_authors,
            'book_id': book.id,
            'genre': book.genres,
        }
        product_items.append(product_item)

    return JsonResponse(product_items, safe=False)
    # return HttpResponse(serializers.serialize('json', favorit_books))

def add_book_favorit_ajax(request, book_id):
    if request.method == 'POST':
        book = Book.objects.get(pk=book_id)
        user = request.user
        existing_favorit = Category.objects.filter(user=request.user, books__id=book_id).first()

        if existing_favorit:
            return HttpResponse("Book is already in favorit list", status=201)

        new_product = Category(books = book, is_favorite = True, user=user)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def delete_favorit(request, book_id):
    user = request.user

    print("User:", user)
    print("Book ID:", book_id)
    existing_favorit = Category.objects.filter(user=user, books__id=book_id).first()
    print("Existing Favorit:", existing_favorit)
    
    if existing_favorit:
        existing_favorit.delete()  # Menghapus item favorit
        return HttpResponse("Book removed from favorit list", status=200)
    else:
        print("ih")
        return HttpResponse("Book is not in favorit list", status=404)
