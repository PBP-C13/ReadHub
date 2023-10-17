from django.db import models
from book.models import Book

# Create your models here.
class Category(models.Model):
    name_category = models.CharField(max_length=100) #untuk nama kateogri nya, misal popular books atau berdasarkan genre.
    books = models.ManyToManyField(Book, related_name='categories') #untuk menghubungkan models Book ke cateogry.
