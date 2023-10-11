from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers

from .models import Book

# Create your views here.

def get_json(self):
    data = Book.objects.filter(pk=1)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")