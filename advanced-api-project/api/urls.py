from django.urls import path
from .views import BookListCreateAPIView, BookRetrieveUpdateDestroyAPIView


urlpatterns = [
    # the url maps to view that lists all books and allows creating a new one
    path('books/', views.BookListCreateAPIView.as_view(), name='books/create'),

    # URL maps to the view that retrieves, updates, or deletes a specific book.
    # The <int:pk> part captures the primary key from the URL.
    path('books/<int:pk>/delete/',
         BookRetreiveUpdateDestroyAPUView.as_view(), name='books/delete',),
    path('books/<int:pk>/update/',
         BookRetreiveUpdateDestroyAPUView.as_view(), name='books/update',),
]
