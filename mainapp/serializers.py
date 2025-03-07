from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Feedback, PublicFeedback, DiscussionPost, DiscussionComment, Report

User = get_user_model()

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"




# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]

# Feedback Serializer
class FeedbackSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Feedback
        fields = ["id", "user", "service", "rating", "comments", "created_at"]

# Public Feedback Serializer
class PublicFeedbackSerializer(serializers.ModelSerializer):
    feedback = FeedbackSerializer(read_only=True)

    class Meta:
        model = PublicFeedback
        fields = ["id", "feedback", "is_public"]

# Discussion Post Serializer
class DiscussionPostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = DiscussionPost
        fields = ["id", "user", "title", "content", "created_at"]

# Discussion Comment Serializer
class DiscussionCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    post = serializers.PrimaryKeyRelatedField(queryset=DiscussionPost.objects.all())

    class Meta:
        model = DiscussionComment
        fields = ["id", "post", "user", "comment", "created_at"]

# Report Serializer
class ReportSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Report
        fields = ["id", "user", "name", "city", "phone_number", "latitude", "longitude", "description", "status", "created_at"]
