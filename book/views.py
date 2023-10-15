from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers

from .models import Book

# Create your views here.
def show_book(request):
    book = Book.objects.filter(pk__in=range(1, 1001))

    context = {
        'name': 'Pak Bepe',
        'class': 'PBP C', 
        'book': book
    }
    return render(request,"book.html", context)

def get_json(self):
    data = Book.objects.filter(pk=1)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")