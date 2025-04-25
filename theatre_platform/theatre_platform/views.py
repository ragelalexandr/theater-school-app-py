# theatre_platform/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def registration(request):
    # Пока что просто отображаем шаблон, форму можно добавить позже.
    return render(request, 'registration.html')

