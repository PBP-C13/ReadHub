from django.db import models
from book.models import Book

class Forum(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    text = models.TextField()