from django.db import models
from book.models import Book

class Detail(models.Model):
    book_authors = models.TextField(null=True, blank=True)
    book_desc = models.TextField(null=True, blank=True)
    book_edition = models.TextField(null=True, blank=True)
    book_format = models.TextField(null=True, blank=True)
    book_isbn = models.TextField(null=True, blank=True)
    book_pages = models.TextField(null=True, blank=True)
    book_rating = models.FloatField(null=True, blank=True)
    book_rating_count = models.IntegerField(null=True, blank=True)
    book_review_count = models.IntegerField(null=True, blank=True)
    book_title = models.TextField(null=True, blank=True)
    genres = models.TextField(null=True, blank=True)
    image_url = models.TextField(null=True, blank=True)