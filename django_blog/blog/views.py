from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
# Import your custom form
from .forms import UserRegistrationForm, PostForm  # import new postform
# class based views
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from django.urls import reverse_lazy  # Used for redirects in CBVs


# home view
def home(request):
    """Basic view to display the home page using base.html."""
    return render(request, 'blog/base.html', {})


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

# CRUD using class based views


class PostListView(ListView):
    """Displays a list of all blog posts."""
    model = Post
    template_name = 'blog/post_list.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'  # Name of the list object in the template
    ordering = ['-published_date']  # Order by newest first


class PostDetailView(DetailView):
    """Displays the content of a single blog post."""
    model = Post
    template_name = 'blog/post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    """Allows authenticated users to create a new post."""
    model = Post
    form_class = PostForm  # Use the custom ModelForm
    template_name = 'blog/post_form.html'

    # Override the form validation to automatically set the author
    def form_valid(self, form):
        # Set the post's author to the logged-in user
        form.instance.author = self.request.user
        return super().form_valid(form)  # Continue form validation process


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Allows post authors to edit their posts."""
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    # Override the form validation to automatically set the author
    def form_valid(self, form):
        # Ensure author remains the logged-in user
        form.instance.author = self.request.user
        return super().form_valid(form)

    # UserPassesTestMixin: Check if the current user is the author of the post
    def test_func(self):
        post = self.get_object()  # Get the post being updated
        # Return True if the current user is the post's author
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Allows post authors to delete their posts."""
    model = Post
    # Template to ask for confirmation
    template_name = 'blog/post_confirm_delete.html'
    # URL to redirect to after successful deletion (use reverse_lazy with CBVs)
    success_url = reverse_lazy('home')

    # Use UserPassesTestMixin: Check if the current user is the author of the post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author
        return True
        return False
