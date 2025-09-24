from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# This view handles retrieving a list of books and creating a new book.


class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # For a list view, only authenticated users can create (post), but anyone can view (get).

# This view handles retrieving, updating, and deleting a single book.


class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    # This view requires authentication for all actions (GET, PUT, DELETE).
