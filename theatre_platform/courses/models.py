from django.db import models

# Create your models here.

from django.db import models
from django.conf import settings

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='courses')
    start_date = models.DateField()
    end_date = models.DateField()
    time = models.TimeField()
    personal_or_pair = models.CharField(max_length=10, choices=[('personal', 'Персональное'), ('pair', 'Парное')])
    # Дополнительно: доступность, записи, лимит мест и т.д.
    
    def __str__(self):
        return self.title
    
class Enrollment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Ожидание'),
        ('confirmed', 'Подтверждено'),
        ('completed', 'Завершено'),
        ('declined', 'Отклонено'),
    ]
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    enrollment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    
    def __str__(self):
        return f"{self.student} -> {self.course} ({self.status})"

