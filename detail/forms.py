from django.forms import ModelForm
from django import forms
from .models import Detail, Review
from book.models import Book

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review']

        