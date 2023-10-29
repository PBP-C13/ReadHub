from django.db import models

class Detail(models.Model):
    similar_books =  models.TextField(null=True, blank=True)
    
class Review(models.Model):
    review = models.ForeignKey(Detail, on_delete=models.CASCADE)