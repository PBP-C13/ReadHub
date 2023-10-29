from django.forms import ModelForm
from django import forms
from .models import Forum
from book.models import Book

class ForumForm(forms.ModelForm):
    book = forms.ModelChoiceField(
        queryset=Book.objects.filter(pk__gte=0, pk__lte=100),
        label="Pilih Buku",
        required=True,
        empty_label="Pilih Buku"
    )
    class Meta:
        model = Forum
        fields = ['text', 'book']
        