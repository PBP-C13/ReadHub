from django.db import models
from book.models import Book
from datetime import datetime, timedelta

# Create your models here.
class BorrowedBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_duration = models.IntegerField()
    return_date = models.DateTimeField(default=datetime.now() + timedelta(days=borrow_duration))
    terms_accepted = models.BooleanField(default=False)


    