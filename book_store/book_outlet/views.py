from django.shortcuts import render
from django.http import Http404, HttpResponse
from .models import Book


def index(request):
    books=Book.objects.all()
    return render(request, 'book_outlet/index.html',{
        'books':books
    })

def book_details(request, id):
    try:
        book = Book.objects.get(id=id)
    except:
        raise Http404    
    return render(request, 'book_outlet/book_details.html', {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestseller": book.is_bestselling
    })