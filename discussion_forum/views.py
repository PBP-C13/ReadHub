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


# Create your views here.
@login_required
def show_forum(request):
    book = Book.objects.all()
    forum = Forum.objects.all()

    context = {
        'name': request.user.username,
        'forum':forum,
        'pilihan': book,
    }

    return render(request, "forum.html", context)

@csrf_exempt
def create_forum(request):
    if request.method == 'POST':
        text = request.POST.get("text")
        book_id = request.POST.get("book_id")
        book = Book.objects.get(id=book_id)
        forum = Forum(author=request.user, book=book, text=text)
        forum.save()

        # Kirim respons JSON dengan data forum yang baru saja dibuat
        data = {
            "author": forum.author.username,
            "text": forum.text,
            "book_title": forum.book.title,
            "book_author": forum.book.author,
        }

        return JsonResponse(data)
    else:
        return JsonResponse({"error": "Invalid request method"})

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

@csrf_exempt
def like_comment(request):
    if request.method == 'POST':
        comment_id = request.POST.get("comment_id")
        comment = get_object_or_404(ForumComment, id=comment_id)
        comment.likes.add(request.user)
        return JsonResponse({"message": "Comment liked successfully!"})

    return JsonResponse({"error": "Invalid request method"})

@csrf_exempt
def unlike_comment(request):
    if request.method == 'POST':
        comment_id = request.POST.get("comment_id")
        comment = get_object_or_404(ForumComment, id=comment_id)
        comment.likes.remove(request.user)
        return JsonResponse({"message": "Comment unliked successfully!"})

    return JsonResponse({"error": "Invalid request method"})

def get_json(self):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

