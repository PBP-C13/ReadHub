from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers
from .models import favorit
from book.models import Book



# Create your views here.

def show_favorit(request):
    favorits = Book.objects.filter(pk__in=range(1, 101))

    context = {
        'name': request.user.username,
        'class': 'PBP C', # Kelas PBP kamu
        'favorit': favorits
    }

    return render(request, "favorit.html", context)

def get_json(self):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
