from django.db import models

class Detail(models.Model):
    similar_books =  models.TextField(null=True, blank=True)
    review = models.TextField(null=True, blank=True)
    
