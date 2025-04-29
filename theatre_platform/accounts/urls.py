# theatre_platform/urls.py

from django.contrib import admin
from django.urls import path, include
from accounts import views as account_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', account_views.home, name='home'),
    path('register/', account_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),
    path('profile/edit/', account_views.edit_profile, name='edit_profile'),
    path('schedule/', account_views.ScheduleListView.as_view(), name='schedule'),
    path('enroll/<int:course_id>/', account_views.enroll_course, name='enroll_course'),
    path('portfolio/add/', account_views.add_portfolio_item, name='add_portfolio'),
    path('history/', account_views.EnrollmentHistoryView.as_view(), name='enrollment_history'),
    path('review/<int:course_id>/', account_views.add_review, name='add_review'),
]
