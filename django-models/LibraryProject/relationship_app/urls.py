from django.urls import path
from .views import list_books, LibraryDetailView, register, login, logout
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    # URL for the list of all books (function-based view)
    path('books/', list_books, name='list_books'),

    # URL for library details (class-based view)
    path('library/<int:pk>/', LibraryDetailView.as_view(),
         name='library_detail'),

    # Authentication URLs
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('register/', views.register, name='register'),

    # role based views
    path('admin-dashboard/', admin_view, name='admin_view'),
    path('librarian-dashboard/', librarian_view, name='librarian_view'),
    path('member-dashboard/', member_view, name='member_view'),
]
