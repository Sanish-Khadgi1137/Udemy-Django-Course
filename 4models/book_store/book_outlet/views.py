from django.shortcuts import render, get_object_or_404

from .models import Book

from django.http import Http404

from django.db.models import Avg, Min, Max

# Create your views here.

def index(request):
                              #order_by() to order the data diplay, "-" is for descending order
    books=Book.objects.all().order_by("-title")#this line fetch data from database and save to cache here"books"
    
    #for more meta data
    #num_books = Book.objects.all().count()
    num_books = books.count()#using cache/variable here "books" to decrease data number of fetching from db
    avg_rating = books.aggregate(Avg("rating")) #we can also use Min Max this way
    return render(request, "book_outlet/index.html", {
        "book1" : books,
        #for more meta data
        "total_number_of_books": num_books,
        "average_rating":avg_rating

    })

# def book_detail(request, id):
def book_detail(request, slug):#we use slug instead of id(unique identifier for each dataset) becuase it is search friendly


    # try:
    #     book=Book.objects.get(pk=id)
    # except:
    #     raise Http404 
      
    #or do
    # book2 = get_object_or_404(Book, pk=id)
    book2 = get_object_or_404(Book, slug=slug) 
    #attribute=parameter


    return render(request, "book_outlet/book_detail.html",{
        "title": book2.title,
        "author": book2.author,
        "rating": book2.rating,
        "is_bestseller": book2.is_bestselling
    } )