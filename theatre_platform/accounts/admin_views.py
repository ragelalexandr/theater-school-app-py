from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.admin.views.decorators import staff_member_required
from accounts.models import Performance, Course, CustomUser, Review
from accounts.forms import PerformanceForm, CourseForm

# Главная страница админ-раздела
@staff_member_required
def admin_dashboard(request):
    context = {
        'performances_count': Performance.objects.count(),
        'courses_count': Course.objects.count(),
        'teachers_count': CustomUser.objects.filter(is_teacher=True).count(),
        'students_count': CustomUser.objects.filter(is_student=True).count(),
        'pending_reviews_count': Review.objects.filter(moderation_status='pending').count(),
    }
    return render(request, 'admin/dashboard.html', context)

# Управление театральными представлениями
@staff_member_required
def performance_list(request):
    performances = Performance.objects.all()
    return render(request, 'admin/performances_list.html', {'performances': performances})

@staff_member_required
def performance_create(request):
    if request.method == 'POST':
        form = PerformanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('performance_list')
    else:
        form = PerformanceForm()
    return render(request, 'admin/performance_form.html', {'form': form})

@staff_member_required
def performance_edit(request, pk):
    performance = get_object_or_404(Performance, pk=pk)
    if request.method == 'POST':
        form = PerformanceForm(request.POST, instance=performance)
        if form.is_valid():
            form.save()
            return redirect('performance_list')
    else:
        form = PerformanceForm(instance=performance)
    return render(request, 'admin/performance_form.html', {'form': form})

@staff_member_required
def performance_delete(request, pk):
    performance = get_object_or_404(Performance, pk=pk)
    if request.method == 'POST':
        performance.delete()
        return redirect('performance_list')
    return render(request, 'admin/performance_confirm_delete.html', {'performance': performance})

# Управление курсами
@staff_member_required
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'admin/course_list.html', {'courses': courses})

@staff_member_required
def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'admin/course_form.html', {'form': form})

@staff_member_required
def course_edit(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)
    return render(request, 'admin/course_form.html', {'form': form})

@staff_member_required
def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    return render(request, 'admin/course_confirm_delete.html', {'course': course})

# Управление преподавателями: список преподавателей
@staff_member_required
def teacher_list(request):
    teachers = CustomUser.objects.filter(is_teacher=True)
    return render(request, 'admin/teacher_list.html', {'teachers': teachers})

# Управление студентами: список студентов
@staff_member_required
def student_list(request):
    students = CustomUser.objects.filter(is_student=True)
    return render(request, 'admin/student_list.html', {'students': students})

# Модерация отзывов
@staff_member_required
def review_list(request):
    # Можно выводить как все отзывы, так и только отзывы, ожидающие модерации
    reviews = Review.objects.all()
    return render(request, 'admin/review_list.html', {'reviews': reviews})

@staff_member_required
def review_moderate(request, pk, action):
    review = get_object_or_404(Review, pk=pk)
    if action == 'approve':
        review.moderation_status = 'approved'
    elif action == 'reject':
        review.moderation_status = 'rejected'
    review.save()
    return redirect('review_list')
