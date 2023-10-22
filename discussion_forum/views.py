from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers
from .models import bookform
from book.models import Book

# Create your views here.

def show_forum(request):
    book = Book.objects.all()

    context = {
        'community': book
    }

    return render(request, "forum.html", context)

def get_json(self):
    data = bookform.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
