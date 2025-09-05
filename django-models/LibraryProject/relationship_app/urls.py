from django.urls import path
from . import views
from .views import LibraryDetailView
from .views import list_books
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

from .views import login_view
from .views import logout_view
from .views import register_view


urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(),
         name='library-detail'),

    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', register_view, name='register'),
]
