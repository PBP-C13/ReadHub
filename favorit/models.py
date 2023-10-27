from django.db import models
from book.models import Book

class favorit(models.Model):
    books = models.ManyToManyField(Book, related_name='favorit') #untuk menghubungkan models Book ke cateogry.
    amountOfBooks = models.IntegerField()
