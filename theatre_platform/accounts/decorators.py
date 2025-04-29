# accounts/decorators.py
from functools import wraps
from django.shortcuts import redirect

def teacher_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_teacher:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('login')
    return _wrapped_view
