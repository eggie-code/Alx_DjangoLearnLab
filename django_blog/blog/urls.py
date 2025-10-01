from django.urls import path, include
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)  # Import the new CBVs

urlpatterns = [
    # General Blog Paths
    path('', views.home, name='home'),

    # Custom Registration Path
    path('register/', views.register, name='register'),

    # Django's Built-in Authentication URLs (for Login/Logout/Password Reset)
    # The 'login' and 'logout' names are automatically generated
    path('', include('django.contrib.auth.urls')),

    # Custom Profile Path
    path('profile/', views.profile, name='profile'),

    path('', PostListView.as_view(), name='home'),  # list view

    path('post/new/', PostCreateView.as_view(), name='post-create'),  # new post

    path('post/<int:pk>/', PostDetailView.as_view(),
         name='post-detail'),  # detail view

    path('post/<int:pk>/edit/', PostUpdateView.as_view(),
         name='post-update'),  # edit post

    path('post/<int:pk>/delete/', PostDeleteView.as_view(),
         name='post-delete'),  # delete post



]
