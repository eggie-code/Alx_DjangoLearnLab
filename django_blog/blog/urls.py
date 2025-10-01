from django.urls import path, include
from . import views

urlpatterns = [
    # General Blog Paths
    path('', views.home, name='home'),

    # Custom Registration Path
    path('register/', views.register, name='register'),

    # Django's Built-in Authentication URLs (for Login/Logout/Password Reset)
    # The 'login' and 'logout' names are automatically generated here.
    path('', include('django.contrib.auth.urls')),

    # Custom Profile Path
    path('profile/', views.profile, name='profile'),
]
