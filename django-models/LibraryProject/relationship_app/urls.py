from django.urls import path
from . import views


urlpatterns = [
    path('books/', views.list_books, name='book-list'),
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(),
         name='library-detail'),
]
