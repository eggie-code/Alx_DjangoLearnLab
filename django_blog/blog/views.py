from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
# Import your custom form
from .forms import UserRegistrationForm

# ... (your existing 'home' view) ...


def register(request):
    """
    Handles user registration using the custom UserRegistrationForm.
    """
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data['email']
            user.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Account created for {username}! You can now log in.')
            return redirect('login')  # Redirect to the 'login' URL name
    else:
        form = UserRegistrationForm()

    return render(request, 'blog/register.html', {'form': form, 'title': 'Register'})


@login_required
def profile(request):
    """
    Allows authenticated users to view their profile page.
    """
    return render(request, 'blog/profile.html', {'title': 'Profile'})
