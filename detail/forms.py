
from django.forms import ModelForm
from django import forms
from .models import Detail
from book.models import Book

class DetailForm(forms.ModelForm):
    book = forms.ModelChoiceField(
        queryset=Book.objects.filter(pk__gte=0, pk__lte=100),
    )
    fields = ('id', 'book_title', 'book_authors', 'genres', 'book_rating', ' book_rating_count', 'book_pages')