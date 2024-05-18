from django.contrib import admin
from .models import Author, Book
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_filter=("author","rating")
admin.site.register(Book,BookAdmin)
admin.site.register(Author)