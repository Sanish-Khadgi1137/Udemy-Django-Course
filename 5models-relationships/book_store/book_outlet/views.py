from django.shortcuts import render, get_object_or_404
from .models import Book
from django.db.models import Avg


def index(request):

    books = Book.objects.all().order_by("-title")
    num_books = books.count()
    avg_rating = books.aggregate(Avg("rating"))
    
    return render(request, "book_outlet/index.html", {
        "book1": books,
        "total_number_of_books": num_books,
        "average_rating": avg_rating
    })


def book_detail(request, slug):

    book2 = get_object_or_404(Book, slug=slug)
    return render(request, "book_outlet/book_detail.html", {
        "title": book2.title,
        "author": book2.author,
        "rating": book2.rating,
        "is_bestseller": book2.is_bestselling
    })
