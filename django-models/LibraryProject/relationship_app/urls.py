from django.urls import path
from .views import book_list, LibraryDetailView

urlpatterns = [
    # URL for the list of all books (function-based view)
    path('books/', book_list, name='book_list'),

    # URL for library details (class-based view)
    path('library/<int:pk>/', LibraryDetailView.as_view(),
         name='library_detail'),
]
