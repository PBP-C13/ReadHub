from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from main.forms import ProductForm
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers
from .models import Forum
from book.models import Book
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ForumForm


# Create your views here.
def show_forum(request):
    book = Book.objects.filter(pk__in=range(1, 101))

    # Dapatkan genre yang sedang aktif dari parameter URL
    active_genre = request.GET.get('genre', None)

    # Filter forum berdasarkan genre yang sedang aktif
    if active_genre:
        forum = Forum.objects.filter(book__genres__icontains=active_genre)
    else:
        forum = Forum.objects.all()

    context = {
        'name': request.user.username,
        'forum':forum,
        'pilihan': book,
        'form': ForumForm()
    }

    return render(request, "forum.html", context)


#Create Forum
def create_forum(request):
    form =  ForumForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    

    context = {'form': form}
    return render(request, "create_forum.html", context)

#Get Product

def get_product_json(request):
    selected_genre = request.GET.get('selected_genre') 

    product_items = []
    forums = Forum.objects.all()

    if selected_genre:
        forums = forums.filter(book__genres=selected_genre)
    
    for forum in forums:
        book = Book.objects.get(id=forum.book_id)  # Gantilah 'book_id' sesuai dengan nama field yang menghubungkan Forum dan Book

        # Buat dictionary baru dengan data forum dan buku
        product_item = {
            'forum_id': forum.text,
            'book_image':book.image_url,
            'book_title': book.book_title,
            'book_author': book.book_authors,
            'book_genre': split_genre(book.genres),
        }

        product_items.append(product_item)

    return JsonResponse(product_items, safe=False)


def split_genre(genre_string):
    if genre_string:
        return genre_string.split('|')
    else:
        return []

#Remove Forum
@csrf_exempt
def remove_forum_ajax(request, id):
    Forum.objects.filter(pk=id).delete()
    return HttpResponseRedirect(reverse("main:show_main"))



@csrf_exempt
def like_forum(request):
    if request.method == 'POST':
        forum_id = request.POST.get("forum_id")
        forum = get_object_or_404(Forum, id=forum_id)
        forum.likes.add(request.user)
        return JsonResponse({"message": "Forum liked successfully!"})

    return JsonResponse({"error": "Invalid request method"})

@csrf_exempt
def unlike_forum(request):
    if request.method == 'POST':
        forum_id = request.POST.get("forum_id")
        forum = get_object_or_404(Forum, id=forum_id)
        forum.likes.remove(request.user)
        return JsonResponse({"message": "Forum unliked successfully!"})

    return JsonResponse({"error": "Invalid request method"})

def get_json(self):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

