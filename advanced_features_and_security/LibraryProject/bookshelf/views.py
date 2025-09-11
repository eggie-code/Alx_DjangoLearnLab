from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .models import Book, Library, UserProfile
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import permission_required, user_passes_test
from django.http import HttpResponse
from .models import Library, Book


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


def is_admin(user):
    return user.is_authenticated and user.userprofile.role == 'Admin'


def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == 'Librarian'


def is_member(user):
    return user.is_authenticated and user.userprofile.role == 'Member'

# Role-based views


@user_passes_test(is_admin)
def admin_view(request):
    """View only accessible by Admin users."""
    return render(request, 'relationship_app/admin_view.html')


@user_passes_test(is_librarian)
def librarian_view(request):
    """View only accessible by Librarian users."""
    return render(request, 'relationship_app/librarian_view.html')


@user_passes_test(is_member)
def member_view(request):
    """View only accessible by Member users."""
    return render(request, 'relationship_app/member_view.html')


@permission_required('relationship_app.can_add_book')
def add_book(request):
    """View to add a new book. Only users with the 'can_add_book' permission can access."""
    # This is a placeholder. A real view would handle a form submission.
    if request.method == "POST":
        return HttpResponse("Book added successfully!")
    return render(request, 'relationship_app/add_book.html')


@permission_required('relationship_app.can_change_book')
def edit_book(request, pk):
    """View to edit an existing book. Only users with 'can_change_book' can access."""
    book = get_object_or_404(Book, pk=pk)
    # This is a placeholder. A real view would handle a form submission.
    if request.method == "POST":
        return HttpResponse(f"Book '{book.title}' edited successfully!")
    return render(request, 'relationship_app/edit_book.html', {'book': book})


@permission_required('relationship_app.can_delete_book')
def delete_book(request, pk):
    """View to delete a book. Only users with 'can_delete_book' can access."""
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return HttpResponse("Book deleted successfully!")
    return render(request, 'relationship_app/delete_book_confirm.html', {'book': book})


# Create your views here.
