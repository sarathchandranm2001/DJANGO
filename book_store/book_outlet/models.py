from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.urls import reverse

# Create your models here.

class Author(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)



class Book(models.Model):
    title = models.CharField(max_length=50)
    rating=models.IntegerField(
        validators=[MinValueValidator(1),MaxValueValidator(5)])
    author =models.ForeignKey(Author,on_delete=models.CASCADE,null=True)
    is_bestselling=models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("book-details", args=[self.id])#other way of giving url as links in stead of href so im commenting it there on views.py
    

def __str__(self):
    return f"{self.title}({self.rating})"

