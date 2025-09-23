from django.urls import path
from .views import list_books, LibraryDetailView, register, login, logout
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import is_admin, is_librarian, is_member, admin_view, librarian_view, member_view
from .views import add_book, edit_book, delete_book
from django.contrib.auth.decorators import user_passes_test, permission_required


urlpatterns = [
    # URL for the list of all books (function-based view)
    path('books/', list_books, name='list_books'),

    # URL for library details (class-based view)
    path('library/<int:pk>/', LibraryDetailView.as_view(),
         name='library_detail'),

    # Authentication URLs
    path('logout/', LogoutView.as_view(template_name='bookshelf/logout.html'), name='logout'),
    path('login/', LoginView.as_view(template_name='bookshelf/login.html'), name='login'),
    path('register/', views.register, name='register'),

    # role based views
    path('admin-dashboard/', admin_view, name='admin_view'),
    path('librarian-dashboard/', librarian_view, name='librarian_view'),
    path('member-dashboard/', member_view, name='member_view'),

    # URLs for custom permission-based views
    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:pk>/', edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', delete_book, name='delete_book'),

]
