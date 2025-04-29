# theatre_platform/accounts/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_student = models.BooleanField(default=True)
    is_teacher = models.BooleanField(default=False)
    
    # Если возникают конфликты для `groups` и `user_permissions`,
    # можно явно указать related_name:
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',
        blank=True
    )

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True)
    photo = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    
    def __str__(self):
        return self.user.username

class Course(models.Model):
    title = models.CharField(max_length=200)
    teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'is_teacher': True})
    start_date = models.DateField()
    end_date = models.DateField()
    available = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title

class Enrollment(models.Model):
    PERSONAL = 'personal'
    GROUP = 'group'
    LEARNING_CHOICES = [
        (PERSONAL, 'Персональное'),
        (GROUP, 'Парное')
    ]
    
    PENDING = 'pending'
    APPROVED = 'approved'
    COMPLETED = 'completed'
    STATUS_CHOICES = [
        (PENDING, 'Ожидание'),
        (APPROVED, 'Подтверждено'),
        (COMPLETED, 'Завершено')
    ]
    
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    type_of_learning = models.CharField(max_length=20, choices=LEARNING_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)
    
    def __str__(self):
        return f"{self.student.username} - {self.course.title}"

class Portfolio(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='portfolio/', blank=True, null=True)
    video = models.FileField(upload_to='portfolio_videos/', blank=True, null=True)
    
    def __str__(self):
        return f"Portfolio of {self.student.username}"

class Review(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Отзыв от {self.student.username} о {self.course.title}"
    
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
