from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from .models import Feedback, PublicFeedback, DiscussionPost, DiscussionComment, Report
from django.conf import settings
from .forms import FeedbackForm, DiscussionPostForm, DiscussionCommentForm, ReportForm

# View for user registration

def home(request):
    return render(request, "home.html")

def register(request):
    if request.method == "POST":
        print(request.POST)
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto login after registration
            return redirect("login")
        else:
            print(form.error_messages)
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})

# View for user login
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("dashboard")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

@login_required
def user_logout(request):
    logout(request)
    return redirect("login")

# View for feedback submission
@login_required
def submit_feedback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user  # Assign the logged-in user
            feedback.save()
            return redirect("feedback_list")  # Redirect to feedback list
    else:
        form = FeedbackForm()
    return render(request, "submit_feedback.html", {"form": form})

# View for displaying public feedback
def feedback_list(request):
    feedbacks = PublicFeedback.objects.filter(is_public=True)
    return render(request, "feedback_list.html", {"feedbacks": feedbacks})

# View for community discussions
@login_required
def discussion_list(request):
    discussions = DiscussionPost.objects.all()
    return render(request, "discussion_list.html", {"discussions": discussions})

@login_required
def discussion_detail(request, pk):
    post = get_object_or_404(DiscussionPost, pk=pk)
    comments = post.comments.all()
    if request.method == "POST":
        form = DiscussionCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect("discussion_detail", pk=post.pk)
    else:
        form = DiscussionCommentForm()
    return render(request, "discussion_detail.html", {"post": post, "comments": comments, "form": form})

# View for reporting an issue
@login_required
def report_issue(request):
    if request.method == "POST":
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user
            report.save()
            return redirect("report_list")
    else:
        form = ReportForm()
    return render(request, "report_issue.html", {"form": form})

# View for listing reports
@login_required
def report_list(request):
    reports = Report.objects.filter(user=request.user)
    return render(request, "report_list.html", {"reports": reports})

@login_required
def dashboard(request):
        issues = Report.objects.filter(user=request.user)
        return render(request, "dashboard.html", {"issues": issues})
        
@login_required
def issueform(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user
            report.save()
            return redirect('dashboard')
        else:
            print(form.errors)
    return render(request, "issueform.html")

@login_required
def report_detail(request, report_id):
    """
    View function to display the detailed report page.
    """
    report = get_object_or_404(Report, id=report_id)
    
    return render(request, "reportdetails.html", {"report": report})

@login_required
def editprofile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            # Add any additional processing here
            user.save()
            return redirect('dashboard')
    else:
        form = UserChangeForm(instance=request.user)
    return render(request, "editprofile.html", {"form": form})