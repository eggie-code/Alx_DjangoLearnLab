from django.urls import path
from . import views
from .views import LibraryDetailView
from .views import list_books
from .views import login_view
from .views import logout_view
from .views import register_view


urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(),
         name='library-detail'),

    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
]
