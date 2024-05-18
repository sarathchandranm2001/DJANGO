from django.contrib import admin
from .models import Adress, Author, Book, Country
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_filter=("author","rating")
admin.site.register(Book,BookAdmin)
admin.site.register(Author)
admin.site.register(Adress)
admin.site.register(Country)


