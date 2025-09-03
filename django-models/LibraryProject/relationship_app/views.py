from django.shortcuts import render
from gjango.views.generic import DetailView
from .models import Book, Library

# list all books


def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})


class LibraryDetailsView(DetailView):
    model = Library
    template_name = 'library_details.html'
    context_object_name = 'library'
