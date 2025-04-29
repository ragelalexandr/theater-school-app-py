# theatre_platform/urls.py

from django.contrib import admin
from django.urls import path, include
from accounts import views as account_views
from django.contrib.auth import views as auth_views
from django.urls import path
from accounts.admin_views import (
    admin_dashboard,
    performance_list, performance_create, performance_edit, performance_delete,
    course_list, course_create, course_edit, course_delete,
    teacher_list, student_list,
    review_list, review_moderate
)

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
    path('dashboard/', admin_dashboard, name='admin_dashboard'),
    # Представления
    path('performances/', performance_list, name='performance_list'),
    path('performances/add/', performance_create, name='performance_create'),
    path('performances/edit/<int:pk>/', performance_edit, name='performance_edit'),
    path('performances/delete/<int:pk>/', performance_delete, name='performance_delete'),
    # Курсы
    path('courses/', course_list, name='course_list'),
    path('courses/add/', course_create, name='course_create'),
    path('courses/edit/<int:pk>/', course_edit, name='course_edit'),
    path('courses/delete/<int:pk>/', course_delete, name='course_delete'),
    # Преподаватели и студенты
    path('teachers/', teacher_list, name='teacher_list'),
    path('students/', student_list, name='student_list'),
    # Отзывы
    path('reviews/', review_list, name='review_list'),
    path('reviews/<int:pk>/<str:action>/', review_moderate, name='review_moderate'),
]