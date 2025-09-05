from django.urls import path
from . import views
from .views import LibraryDetailView
from .views import list_books
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from .views import login_view
from .views import logout_view
from .views import register_view
from .views import add_book, edit_book, delete_book


urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(),
         name='library-detail'),

    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register_view, name='register'),

    path('admin/', views.admin_dashboard, name='admin_view'),
    path('librarian/', views.librarian_dashboard, name='librarian_view'),
    path('member/', views.member_dashboard, name='member_view'),

    path('books/add_book/', add_book, name='add_book'),
    path('books/<int:pk>/edit_book/', edit_book, name='edit_book'),
    path('books/<int:pk>/delete_book/', delete_book, name='delete_book')
]
