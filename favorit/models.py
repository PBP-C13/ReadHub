from django.db import models
from book.models import Book
from django.contrib.auth.models import User

class favorit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book, related_name='favorit') #untuk menghubungkan models Book ke cateogry.
    amountOfBooks = models.IntegerField()
