from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.urls import reverse

# Create your models here.

class Adress(models.Model):
    street=models.CharField(max_length=80)
    postal_code= models.CharField(max_length=5)
    city=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.street},{self.postal_code}"

    class Meta:#advanced class not used often
        verbose_name_plural = "Adress Entries" #not important



class Author(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    adress= models.OneToOneField(Adress, on_delete=models.CASCADE,related_name="author",null=True)#one to one relation

    def full_name(self):
        return self.first_name + "" + self.last_name

    def __str__(self):
       return self.full_name()





class Book(models.Model):
    title = models.CharField(max_length=50)
    rating=models.IntegerField(
        validators=[MinValueValidator(1),MaxValueValidator(5)])
    author =models.ForeignKey(Author,on_delete=models.CASCADE,null=True,related_name="books")
    is_bestselling=models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("book-details", args=[self.id])#other way of giving url as links in stead of href so im commenting it there on views.py
    def __str__(self):
        return f"{self.title}({self.rating})"#to rename object 1 to original name

