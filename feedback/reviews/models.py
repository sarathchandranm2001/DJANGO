from django.db import models

class Review(models.Model):
    name=models.CharField(max_length=100)
    review_text=models.TextField()
    rating=models.IntegerField()

