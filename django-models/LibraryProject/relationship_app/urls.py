from django.urls import path
from . import views

urlpatterns = [
    # URL for the list of all books (function-based view)
    path('books/', views.list_books, name='list_books'),

    # URL for library details (class-based view)
    path('library/<int:pk>/', views.LibraryDetailView.as_view(),
         name='library_detail'),
]
