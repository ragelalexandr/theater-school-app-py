from django.contrib import admin
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'teacher', 'duration')
    search_fields = ('title', 'teacher__name')
    list_filter = ('duration',)
