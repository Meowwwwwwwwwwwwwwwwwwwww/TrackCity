from django.contrib import admin
from .models import Report

# Register your models here.
from django.contrib import admin
from .models import Feedback, PublicFeedback, DiscussionPost, DiscussionComment, Report

# ✅ Registering Feedback with additional customization
@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("user", "service", "rating", "created_at")
    list_filter = ("service", "rating")
    search_fields = ("user__username", "service", "comments")

# ✅ Registering PublicFeedback
@admin.register(PublicFeedback)
class PublicFeedbackAdmin(admin.ModelAdmin):
    list_display = ("feedback", "is_public")
    list_filter = ("is_public",)

# ✅ Registering DiscussionPost
@admin.register(DiscussionPost)
class DiscussionPostAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "created_at")
    search_fields = ("title", "content")
    list_filter = ("created_at",)

# ✅ Registering DiscussionComment
@admin.register(DiscussionComment)
class DiscussionCommentAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "created_at")
    search_fields = ("user__username", "comment")
    list_filter = ("created_at",)

# ✅ Registering Report



admin.site.register(Report)

