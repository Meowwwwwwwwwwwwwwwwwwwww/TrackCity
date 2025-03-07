from django.urls import path
from .views import register, user_login, user_logout, home,dashboard,issueform ,report_detail,editprofile

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('issueform/', issueform, name='issueform'),
    path('report/<int:report_id>/', report_detail, name='report'),

    path('editprofile/', editprofile, name='editprofile'),
    ]