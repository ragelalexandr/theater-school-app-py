"""
URL configuration for theatre_platform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from accounts import views as account_views
from accounts.views import EnrollmentHistoryView
from accounts import views as account_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin-panel/', include('accounts.urls_admin')),
    path('', account_views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', account_views.register, name='register'),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('history/', EnrollmentHistoryView.as_view(), name='history'),
    path('teacher/dashboard/', account_views.teacher_dashboard, name='teacher_dashboard'),
    path('teacher/enrollment/approve/<int:enrollment_id>/', account_views.approve_enrollment, name='approve_enrollment'),
    path('teacher/enrollment/reject/<int:enrollment_id>/', account_views.reject_enrollment, name='reject_enrollment'),
]
