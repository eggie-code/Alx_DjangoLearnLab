from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

User = settings.AUTH_USER_MODEL


class Notification(models.Model):
    recipient = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='notifications')
    # the user who triggered the notification (actor)
    actor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='sent_notifications')
    # e.g. "liked", "commented", "followed"
    verb = models.CharField(max_length=255)
    # generic relation to the target (post, comment, etc.)
    target_content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE, null=True, blank=True)
    target_object_id = models.PositiveIntegerField(null=True, blank=True)
    target = GenericForeignKey('target_content_type', 'target_object_id')
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.recipient} – {self.actor} {self.verb} {self.target}"
