from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from main.forms import ProductForm
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers
from .models import Forum, Like
from book.models import Book
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ForumForm
from django.shortcuts import redirect


def show_forum(request):
    book = Book.objects.filter(pk__in=range(1, 101))
    active_genre = request.GET.get('genre', None)
    forum = Forum.objects.all()

    context = {
        'name': request.user.username,
        'forum':forum,
        'pilihan': book,
        'form': ForumForm()
    }

    return render(request, "forum.html", context)


@login_required(login_url='/login')
def create_forum(request):
    if request.method == "POST":
        form = ForumForm(request.POST)
        if form.is_valid():
            forum = form.save(commit=False)
            forum.author = request.user  # Set author ke pengguna saat ini
            forum.save()
            return HttpResponseRedirect(reverse('discussion_forum:show_forum'))
        else:
            # Handle error in form validation
            # Misalnya, tampilkan pesan kesalahan atau log pesan kesalahan
            print(form.errors)
    else:
        form = ForumForm()

    context = {'form': form}
    return render(request, "create_forum.html", context)

@login_required(login_url='/login')
def get_product_json(request):
    selected_genre = request.GET.get('selected_genre') 
    product_items = []
    forums = Forum.objects.all()

    if selected_genre:
        forums = forums.filter(book__genres=selected_genre)
    
    for forum in forums:
        book = Book.objects.get(id=forum.book_id)  
        # Buat dictionary baru dengan data forum dan buku
        product_item = {
            'name': forum.author.username ,
            'forum_id': forum.id,
            'likes':forum.like,
            'forum_text': forum.text,
            'book_image':book.image_url,
            'book_title': book.book_title,
            'book_author': book.book_authors,
            'book_genre': split_genre(book.genres),
            
        }
        product_items.append(product_item)

    return JsonResponse(product_items, safe=False)

def split_genre(genre_string):
    if genre_string:
        genres = genre_string.split('|')
        genres = [genre.replace(' ', '-') for genre in genres]
        return genres

    else:
        return []

@login_required(login_url='/login')
def toggle_like_forum(request, id):
    forum = Forum.objects.get(id=id)
    user = request.user 

    if user in forum.liked_by.all():
        forum.like -= 1
        forum.liked_by.remove(user)
    else:
        forum.like += 1
        forum.liked_by.add(user)
    
    forum.save()

    response = HttpResponseRedirect(reverse("discussion_forum:show_forum", args=[id]))  # Ganti "forum:show_forum" dengan nama URL yang sesuai
    return response


@login_required(login_url='/login')
def delete_item(request, item_id):
    try:
        item = Forum.objects.get(id=item_id)
        item.delete()
        return JsonResponse({'message': 'Item deleted successfully.'})
    except Forum.DoesNotExist:
        return JsonResponse({'error': 'Item does not exist.'})


@login_required(login_url='/login')
def like_forum_post(request, post_id):
    post = get_object_or_404(Forum, pk=post_id)
    user = request.user

    # Periksa apakah pengguna telah melakukan like pada posting ini
    if Like.objects.filter(user=user, post=post).exists():
        # Jika sudah dilike, kurangi jumlah like
        post.like -= 1
        post.liked_by.remove(user)
        post.save()
        Like.objects.filter(user=user, post=post).delete()
    else:
        # Jika belum dilike, tambahkan like
        post.like += 1
        post.liked_by.add(user)
        post.save()
        Like.objects.create(user=user, post=post)
    return redirect('discussion_forum:show_forum')


def get_json(self):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")