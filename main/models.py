from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    price = models.IntegerField()
    description = models.TextField()
    title = models.CharField (_("title"), max_length=255)
    author = models.CharField (_("author"), max_length=255)
    desc = models.TextField (_("description"))
    format = models.CharField (_("format"), max_length=100)
    isbn = models.IntegerField (_("isbn"))
    pages = models.IntegerField (_("pages"))
    rating = models.IntegerField (_("rating"))
    genre = models.IntegerField(_("genre"))
    image = models.TextField (_("image"),  max_length=255)

class PrivacyPolicy(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title