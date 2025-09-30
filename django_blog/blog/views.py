from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.models import User

# Register view


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('profile')
    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {'form': form})

# Profile view


@login_required
def profile(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        request.user.email = email
        request.user.save()
        messages.success(request, "Profile updated.")
    return render(request, 'blog/profile.html')
