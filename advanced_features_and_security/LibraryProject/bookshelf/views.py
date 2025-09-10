from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Post

# View to list all posts


@permission_required('relationship_app.can_view', raise_exception=True)
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

# View to create a new post


@permission_required('relationship_app.can_create', raise_exception=True)
def post_create(request):
    # Logic to create a post
    if request.method == 'POST':
        # ... process form data
        return redirect('post_list')
    return render(request, 'post_form.html')

# View to edit an existing post


@permission_required('relationship_app.can_edit', raise_exception=True)
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # Logic to edit a post
    if request.method == 'POST':
        # ... process form data
        return redirect('post_list')
    return render(request, 'post_form.html', {'post': post})

# View to delete a post


@permission_required('relationship_app.can_delete', raise_exception=True)
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'post_confirm_delete.html', {'post': post})
# Create your views here.
