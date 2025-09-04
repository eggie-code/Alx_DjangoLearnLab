from django.shortcuts import render

# Create your views here.


def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})
