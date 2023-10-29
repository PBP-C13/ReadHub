from django.forms import ModelForm
from django import forms
from .models import Detail
from book.models import Book

class ReviewForm(forms.ModelForm):
    book = forms.ModelChoiceField(
        queryset=Book.objects.filter(pk__gte=0, pk__lte=100),
        label = "Review Book"
    )
    fields = ['text']