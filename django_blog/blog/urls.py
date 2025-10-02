from django.urls import path, include
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)  # Import  CBVs

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

    path('post/<int:pk>/update/', PostUpdateView.as_view(),
         name='post-update'),  # update post

    path('post/<int:pk>/delete/', PostDeleteView.as_view(),
         name='post-delete'),  # delete post

    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
]


]
