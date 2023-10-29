from django.shortcuts import redirect, render
from django.http import HttpResponseNotFound, HttpResponseRedirect
from category.forms import FavoritForm
from main.forms import ProductForm
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers
from .models import favorit
from book.models import Book



# Create your views here.

def show_favorit(request):
    favorits = favorit.objects.all().values('books')

    context = {
        'name': request.user.username,
        'class': 'PBP C', # Kelas PBP kamu
        'favorit': favorits
    }

    return render(request, "favorit.html", context)


def get_book_json(self):
    data = favorit.objects.all().values('books')
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def add_book_favorit_ajax(request, book_id):
    if request.method == 'POST':
        # Menggunakan form untuk memproses data POST
        form = FavoritForm(request.POST)

        if form.is_valid():
            favorit = form.save(commit=False)
            favorit.user = request.user
            favorit.save()

            return redirect('category/')  # Ubah 'category' sesuai dengan nama URL yang benar
    
    return HttpResponseNotFound()
