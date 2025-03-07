from django import forms
from django.contrib.auth.models import User
from .models import Feedback, DiscussionPost, DiscussionComment, Report


# User Registration Form
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password"]


# User Login Form
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


# Feedback Form
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ["service", "rating", "comments"]


# Discussion Post Form
class DiscussionPostForm(forms.ModelForm):
    class Meta:
        model = DiscussionPost
        fields = ["title", "content"]


# Discussion Comment Form
class DiscussionCommentForm(forms.ModelForm):
    class Meta:
        model = DiscussionComment
        fields = ["comment"]


# Report Submission Form
class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ["description", "user"]
