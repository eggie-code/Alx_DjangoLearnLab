from rest_framework import serializers
from .models import Like, Post
from .models import Comment
from .models import Notification


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())

    class Meta:
        model = Like
        fields = ['id', 'user', 'post', 'created_at']


class NotificationSerializer(serializers.ModelSerializer):
    actor = serializers.ReadOnlyField(source='actor.username')
    # If your target is a post, you might want to show its id or title
    target_id = serializers.IntegerField(
        source='target_object_id', read_only=True)
    target_type = serializers.CharField(
        source='target_content_type.model', read_only=True)

    class Meta:
        model = Notification
        fields = ['id', 'actor', 'verb', 'target_type',
                  'target_id', 'timestamp', 'is_read']
