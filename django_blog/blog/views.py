from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib import messages

# Registration view


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in user after registration
            messages.success(request, 'Registration successful.')
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

# Profile view


@login_required  # User must be logged in to access
def profile(request):
    if request.method == 'POST':
        # Handle profile updates
        email = request.POST.get('email')
        request.user.email = email
        request.user.save()
        messages.success(request, 'Profile updated.')
    return render(request, 'blog/profile.html')
