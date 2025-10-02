from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from .models import User


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blog:index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('blog:index')
    return render(request, 'blog/login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('blog:index')


@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        user.email = request.POST['email']
        user.save()
    return render(request, 'blog/profile.html', {'user': user})
