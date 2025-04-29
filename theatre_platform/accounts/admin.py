# accounts/admin.py

from django.contrib import admin
from .models import CustomUser, Course, Enrollment, Portfolio, Profile, Review

admin.site.register(CustomUser)
admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(Portfolio)
admin.site.register(Profile)
admin.site.register(Review)
