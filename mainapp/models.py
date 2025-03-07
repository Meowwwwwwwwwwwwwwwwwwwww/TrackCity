from django.db import models
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# 1️⃣ Model for Feedback Submission
class Feedback(models.Model):
    SERVICE_CHOICES = [
        ("sanitation", "Sanitation"),
        ("road_maintenance", "Road Maintenance"),
        ("public_transport", "Public Transport"),
        ("electricity", "Electricity"),
        ("water_supply", "Water Supply"),
        ("other", "Other"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Who submitted the feedback
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]  # Restrict to 1-5
    )
    comments = models.TextField()  # Additional feedback
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.service} ({self.rating}⭐)"

# 2️⃣ Model for Viewing Feedback
class PublicFeedback(models.Model):
    feedback = models.OneToOneField(Feedback, on_delete=models.CASCADE)  # Link to Feedback
    is_public = models.BooleanField(default=True)  # Should it be public?
    
    def __str__(self):
        return f"Public Feedback: {self.feedback.service}"

# 3️⃣ Model for Community Discussions
class DiscussionPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Who posted
    title = models.CharField(max_length=200)  # Discussion title
    content = models.TextField()  # Discussion content
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# 4️⃣ Model for Community Comments
class DiscussionComment(models.Model):
    post = models.ForeignKey(DiscussionPost, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.title}"


class Report(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("in_progress", "In Progress"),
        ("resolved", "Resolved"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.description} - ({self.status})"
