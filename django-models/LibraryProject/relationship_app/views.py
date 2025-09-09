from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .models import Book, Library
from django.views.generic import DetailView


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            # Redirect to the book list after registration
            return redirect("list_books")
        messages.error(
            request, "Unsuccessful registration. Invalid information.")
    form = UserCreationForm()
    return render(request=request, template_name="relationship_app/register.html", context={"form": form})


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                # Redirect to the book list after login
                return redirect("list_books")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="relationship_app/login.html", context={"form": form})


def logout(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("login")


def list_books(request):
    """Function-based view to list all books."""
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)


class LibraryDetailView(DetailView):
    """Class-based view to display details for a specific library."""
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
