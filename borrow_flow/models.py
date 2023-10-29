from django.db import models
from book.models import Book
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

# Create your models here.
class BorrowedBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, name='user')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, name='book')
    borrow_duration = models.IntegerField(name='borrow_duration', validators=[MinValueValidator(0)])
    borrow_date = models.DateField(auto_now_add=True, name='borrow_date')
    return_date = models.DateField(name='return_date')
    terms_accepted_1 = models.BooleanField(default=False, name='terms_accepted_1')
    terms_accepted_2 = models.BooleanField(default=False, name='terms_accepted_2')
    terms_accepted_3 = models.BooleanField(default=False, name='terms_accepted_3')