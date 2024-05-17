from django.shortcuts import render
from django.http import Http404
from django.db.models import Avg, Max, Min
from .models import Book

def index(request):
    books = Book.objects.all()
    num_books = books.count()
    avg_rating = books.aggregate(Avg('rating'))['rating__avg']
    return render(request, 'book_outlet/index.html', {
        'books': books,
        'total_books': num_books,
        'avg_rating': avg_rating
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