from django.db import models
from django.core.validators import MinLengthValidator

class Tag(models.Model):
    captions=models.CharField(max_length=20)

    def __str__(self):
        return self.captions


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_adress=models.EmailField()

    def full_name(self):
        return f'{self.first_name} {self.last_name}'
        

    def __str__(self) :
        return self.full_name()
    #maynot be working
class Post(models.Model):
    title=models.CharField(max_length=150)
    excerpt=models.CharField(max_length=200)
    image_name=models.CharField(max_length=100)
    date=models.DateField(auto_now=True)
    slug=models.SlugField(unique=True,db_index=True)
    content=models.TextField(validators=[MinLengthValidator(10)])
    author=models.ForeignKey(Author,on_delete=models.SET_NULL,related_name="posts",null=True)
    tags=models.ManyToManyField(Tag)