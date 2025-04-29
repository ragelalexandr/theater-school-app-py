from django.urls import path
from accounts.admin_views import (
    admin_dashboard,
    performance_list, performance_create, performance_edit, performance_delete,
    course_list, course_create, course_edit, course_delete,
    teacher_list, student_list,
    review_list, review_moderate,
)

urlpatterns = [
    path('dashboard/', admin_dashboard, name='admin_dashboard'),
    # Представления для управления театральными представлениями:
    path('performances/', performance_list, name='performance_list'),
    path('performances/add/', performance_create, name='performance_create'),
    path('performances/edit/<int:pk>/', performance_edit, name='performance_edit'),
    path('performances/delete/<int:pk>/', performance_delete, name='performance_delete'),
    # Курсы:
    path('courses/', course_list, name='course_list'),
    path('courses/add/', course_create, name='course_create'),
    path('courses/edit/<int:pk>/', course_edit, name='course_edit'),
    path('courses/delete/<int:pk>/', course_delete, name='course_delete'),
    # Списки преподавателей и студентов:
    path('teachers/', teacher_list, name='teacher_list'),
    path('students/', student_list, name='student_list'),
    # Модерация отзывов:
    path('reviews/', review_list, name='review_list'),
    path('reviews/<int:pk>/<str:action>/', review_moderate, name='review_moderate'),
]
