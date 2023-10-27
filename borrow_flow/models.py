from django.db import models
from book.models import Book


# Create your models here.
class BorrowedBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_duration = models.IntegerField()
    return_date = models.DateTimeField()
    terms_accepted = models.BooleanField(default=False)


    