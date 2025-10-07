from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType
from django.apps import apps
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners to edit or delete their objects.
    """

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user or request.method in permissions.SAFE_METHODS


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def get_queryset(self):
        Post = apps.get_model('posts', 'Post')
        return Post.objects.all().order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        Comment = apps.get_model('posts', 'Comment')
        return Comment.objects.all().order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_feed(request):
    following_users = request.user.following.all()
    posts = Post.objects.filter(author__in=following_users).order_by
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_post(request, pk):
    Post = apps.get_model('posts', 'Post')
    Like = apps.get_model('posts', 'Like')

    user = request.user
    post = get_object_or_404(Post, pk=pk)

    like, created = Like.objects.get_or_create(user=user, post=post)
    if not created:
        return Response({"detail": "Already liked."}, status=400)

    Notification = apps.get_model('notifications', 'Notification')
    Notification.objects.create(
        recipient=post.author,
        actor=user,
        verb='liked',
        target_object_id=post.id,
        target_content_type=ContentType.objects.get_for_model(post)
    )

    return Response({"detail": "Post liked."})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unlike_post(request, pk):
    Post = apps.get_model('posts', 'Post')
    Like = apps.get_model('posts', 'Like')

    post = get_object_or_404(Post, pk=pk)
    user = request.user

    like = Like.objects.filter(user=user, post=post).first()
    if not like:
        return Response({'detail': 'You have not liked this post.'}, status=400)
    like.delete()
    return Response({'detail': 'Like removed.'}, status=204)
