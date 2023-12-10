from django.db import models
from django.contrib.auth.models import User  
from book.models import Book


class Detail(models.Model):
    similar_books =  models.TextField(null=True, blank=True)
    
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)  # Link to a Book
    review = models.TextField()

class ReviewFlutter(models.Model):
    user = models.TextField()
    book = models.TextField()
    review = models.TextField()
