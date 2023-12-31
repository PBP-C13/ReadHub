import json
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
from django.http import JsonResponse
from django.core.serializers import serialize
from category.models import Category
from django.views.decorators.csrf import csrf_exempt

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
    categories = Category.objects.filter(user=request.user)
    # Ambil semua buku dalam basis data

    context = {
        'name': request.user.username,
        'categories': categories,
    }

    return render(request, "favoritpage.html", context)

# def add_books_to_category(request):
#     category = Category.objects.get(name_category='Fiksi')  # Ganti 'Fiksi' dengan nama kategori yang sesuai
#     books_to_add = Book.objects.filter(genre='Fiksi')  

#     for book in books_to_add:
#         category.books.add(book)

#     return HttpResponse("Buku-buku telah ditambahkan ke kategori Fiksi.")

def show_json_bookfavorit(request):
    data = Category.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# def show_json_favorit(request):
#     # Cetak ID pengguna ke terminal

#     print("User ID:", request.user.id)
#     favorit_books = Category.objects.filter(user=request.user.id)
    
#     # Ambil hanya ID buku dari setiap objek Category
#     book_ids = [favorit.books.pk for favorit in favorit_books]
    
#     # Ambil objek-objek Book yang sesuai
#     books = Book.objects.filter(id__in=book_ids)
    
#     return HttpResponse(serializers.serialize("json", books), content_type="application/json")

def show_json_favorit(request):
    favorit_books = Category.objects.filter(user=request.user.id)
    favorit_book_data = []
    print(request.user)
    for favorit_book in favorit_books:
        book = {
            'id': favorit_book.books.pk,
            'book_authors': favorit_book.books.book_authors,
            'book_desc': favorit_book.books.book_desc,
            'book_edition': favorit_book.books.book_edition,
            'book_format': favorit_book.books.book_format,
            'book_isbn': favorit_book.books.book_isbn,
            'book_pages': favorit_book.books.book_pages,
            'book_rating': favorit_book.books.book_rating,
            'book_rating_count': favorit_book.books.book_rating_count,
            'book_review_count': favorit_book.books.book_review_count,
            'book_title': favorit_book.books.book_title,
            'genres': favorit_book.books.genres,
            'image_url': favorit_book.books.image_url,
        }
        data = {
            'user': favorit_book.user.pk,
            'books': book,
            'name_category': favorit_book.name_category,
            'is_favorit': favorit_book.is_favorite,

        }
        favorit_book_data.append(data)
    
    return JsonResponse(favorit_book_data, safe=False)



#fungsi untuk mengembalikan data jason:
def get_product_json(request):
    all_books = Book.objects.all()[:100]
    return HttpResponse(serializers.serialize('json', all_books))

#untuk dapetin buku2 yang ditambahkan ke favorit
def get_book_favorit(request):
    product_items = []
    favorit_books = Category.objects.filter(user=request.user)
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


@csrf_exempt
def add_favorit_flutter(request, id):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        book = Book.objects.get(pk = data['book']['pk'])

        existing_favorit = Category.objects.filter(user=request.user, books__id= id).first()

        if existing_favorit:
            return JsonResponse({"status": "error"}, status=401)
        
        print(data["isFavorit"])

        if data["isFavorit"]:
            book_favorit = Category.objects.create(
                user = request.user,
                books = book,
                is_favorite = data["isFavorit"]
            )
            book_favorit.save()
            return JsonResponse({"status": "success"}, status=200)
        else:
            return JsonResponse({"status": "no"}, status=401)
    else:
        return JsonResponse({"status": "error"}, status=401)

#untuk delete book favorit
def delete_favorit(request, book_id):
    user = request.user

    existing_favorit = Category.objects.filter(user=user, books__id=book_id).first()

    
    if existing_favorit:
        existing_favorit.delete()  # Menghapus item favorit
        return HttpResponse("Book removed from favorit list", status=200)
    else:
        print("ih")
        return HttpResponse("Book is not in favorit list", status=404)

@csrf_exempt
def delete_favorit_flutter(request, id):
    try:
        favorit_book = Category.objects.filter(user=request.user)
        for book in favorit_book:
            if book.books.pk==id:
                book.delete()
        return JsonResponse({'message': 'Book returned successfully'})
    except favorit_book.DoesNotExist:
        return JsonResponse({'error': 'Book does not exist'})
