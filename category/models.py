from django.db import models
from book.models import Book
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name_category = models.CharField(max_length=100) #untuk nama kateogri nya, misal popular books atau berdasarkan genre.
    user = models.ForeignKey(User, on_delete=models.CASCADE, name='user')
    books = models.ForeignKey(Book, on_delete=models.CASCADE, name='books')
    is_favorite = models.BooleanField(default=False)  # Tambahkan bidang ini
