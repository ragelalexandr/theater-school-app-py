# accounts/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, DateInput
from .models import CustomUser, Profile, Enrollment, Portfolio, Review
from accounts.models import Performance, Course

class PerformanceForm(forms.ModelForm):
    class Meta:
        model = Performance
        fields = ['title', 'date', 'description']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'teacher', 'start_date', 'end_date', 'available']


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'photo']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        # Стандартная форма регистрации предполагает два поля пароля: password1 и password2.
        fields = ('username', 'email', 'password1', 'password2')

class EnrollmentForm(ModelForm):
    class Meta:
        model = Enrollment
        fields = ['type_of_learning', 'start_date', 'end_date']
        widgets = {
            'start_date': DateInput(attrs={'type': 'date'}),
            'end_date': DateInput(attrs={'type': 'date'}),
        }

class PortfolioForm(ModelForm):
    class Meta:
        model = Portfolio
        fields = ['description', 'image', 'video']

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['text']
