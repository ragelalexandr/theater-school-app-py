# theatre_platform/views.py
from django.templatetags.static import static
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def registration(request):
    # Пока что просто отображаем шаблон, форму можно добавить позже.
    return render(request, 'registration/registration.html')

from django.shortcuts import render

def gallery_view(request):
    images = [
        {"url": "/images/slider/image1.png"},
        {"url": "/images/slider/image2.png"},
        {"url": "/images/slider/image3.png"},
        {"url": "/images/slider/image4.png"},
        {"url": "/images/slider/image5.png"},
    ]
    return render(request, "gallery.html", {"images": images})


