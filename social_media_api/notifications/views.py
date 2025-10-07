from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import NotificationSerializer
from django.apps import apps


class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Return notifications for the logged-in user, ordered newest first
        return Notification.objects.filter(recipient=self.request.user).order_by('-timestamp')


class NotificationMarkReadView(generics.UpdateAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Limit to notifications for this user
        return Notification.objects.filter(recipient=self.request.user)

    def perform_update(self, serializer):
        # Mark as read
        serializer.save(is_read=True)

    def create_like_notification(actor, post_id):
    post = Post.objects.get(pk=post_id)
    Notification.objects.create(
        recipient=post.author,
        actor=actor,
        verb='liked',
        target_object_id=post.id,
        target_content_type=ContentType.objects.get_for_model(post)
    )
