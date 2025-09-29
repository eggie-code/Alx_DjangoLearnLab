from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, permissions
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics, filters
from django_filters import rest_framework

# List all books, support filtering, serching and ordering


class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

    filter_backends = [
        DjangoFilterBackend,  # filtering
        filters.SearchFilter,  # searching
        filters.OrderingFilter  # ordering
    ]
    # filterable fields
    filterset_fields = ['title', 'author', 'publication_year']
    # searchable fields
    search_fields = ['title', 'publication_year']
    # orderable fields
    ordering_fields = ['title', 'publication_year']


# DetailView - Read one book by ID (public)


class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

# CreateView - Add a new book (authenticated only)


class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# UpdateView - Modify existing book (authenticated only)


class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# DeleteView - Delete book (authenticated only)


class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# This view handles retrieving a list of books and creating a new book.
class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # For a list view, only authenticated users can create (post), but anyone can view (get).


def perform_create(self, serializer):

    if Book.objects.filter(title=self.request.data.get('title')).exists():
        raise serializers.ValidationError(
            {"title": "A book with this title already exists."})
    serializer.save()

# This view handles retrieving, updating, and deleting a single book.


class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    # This view requires authentication for all actions (GET, PUT, DELETE).
