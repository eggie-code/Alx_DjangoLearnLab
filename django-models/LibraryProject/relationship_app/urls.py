from django.urls import path
from .views import list_books
from .views import LibraryDetailView
from .views import register_request
from .views import login_request
from .views import logout_request


urlpatterns = [
    # URL for the list of all books (function-based view)
    path('books/', list_books, name='list_books'),

    # URL for library details (class-based view)
    path('library/<int:pk>/', LibraryDetailView.as_view(),
         name='library_detail'),

    # Authentication URLs
    path('register/', register_request, name='register'),
    path('login/', login_request, name='login'),
    path('logout/', logout_request, name='logout'),
]
