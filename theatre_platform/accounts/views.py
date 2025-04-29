# accounts/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.http import HttpResponse
from .decorators import teacher_required
from .models import Enrollment, Course
from .forms import (
    CustomUserCreationForm,
    ProfileForm,
    EnrollmentForm,
    PortfolioForm,
    ReviewForm
)




@teacher_required
def teacher_dashboard(request):
    """
    Отображает список курсов, за которые отвечает преподаватель, а также список записей студентов.
    """
    # Получаем курсы, где преподаватель является текущим пользователем
    courses = Course.objects.filter(teacher=request.user)
    # Получаем все записи по этим курсам
    enrollments = Enrollment.objects.filter(course__in=courses)
    
    context = {
        'courses': courses,
        'enrollments': enrollments,
    }
    return render(request, 'accounts/teacher_dashboard.html', context)


@teacher_required
def approve_enrollment(request, enrollment_id):
    """
    Подтверждение записи студента.
    """
    enrollment = get_object_or_404(Enrollment, id=enrollment_id, course__teacher=request.user)
    enrollment.status = Enrollment.APPROVED
    enrollment.save()
    return redirect('teacher_dashboard')


@teacher_required
def reject_enrollment(request, enrollment_id):
    """
    Отклонение записи студента.
    """
    enrollment = get_object_or_404(Enrollment, id=enrollment_id, course__teacher=request.user)
    enrollment.status = Enrollment.DECLINED  # Используем только что добавленный статус 'declined'
    enrollment.save()
    return redirect('teacher_dashboard')


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # После регистрации перенаправляем на страницу входа
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


@login_required
def edit_profile(request):
    profile = request.user.profile
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Убедитесь, что существует страница профиля
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'accounts/edit_profile.html', {'form': form})


@login_required
def enroll_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == "POST":
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            enrollment = form.save(commit=False)
            enrollment.student = request.user
            enrollment.course = course
            enrollment.save()
            return redirect('enrollment_history')
    else:
        form = EnrollmentForm()
    return render(request, 'accounts/enroll_course.html', {'form': form, 'course': course})


class ScheduleListView(ListView):
    model = Course
    template_name = 'accounts/schedule.html'
    context_object_name = 'courses'


class EnrollmentHistoryView(ListView):
    model = Enrollment
    template_name = 'accounts/enrollment_history.html'
    context_object_name = 'enrollments'
    
    def get_queryset(self):
        return Enrollment.objects.filter(student=self.request.user)


@login_required
def add_portfolio_item(request):
    if request.method == "POST":
        form = PortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            portfolio_item = form.save(commit=False)
            portfolio_item.student = request.user
            portfolio_item.save()
            return redirect('portfolio')  # Предполагается, что настроена страница для портфолио
    else:
        form = PortfolioForm()
    return render(request, 'accounts/portfolio_form.html', {'form': form})


@login_required
def add_review(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.student = request.user
            review.course = course
            review.save()
            return redirect('enrollment_history')  # Или можно перенаправить на страницу курса
    else:
        form = ReviewForm()
    return render(request, 'accounts/review_form.html', {'form': form, 'course': course})
