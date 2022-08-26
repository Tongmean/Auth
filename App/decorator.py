from tokenize import group
from urllib import request
from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_User(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('Home')
        else:
            return view_func(request, *args, **kwargs)
    
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                
            if group in allowed_users:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("You are not Authorized")
        return wrapper_func
    return decorator

def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
            
        if group == 'User':
            return HttpResponse('You have Authorize view this Page:')
        
        if group == 'admin':
            return view_func(request, *args, **kwargs)
        
    return wrapper_function

def user_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
            
        if group == 'User':
            return view_func(request, *args, **kwargs)
        
        if group == 'admin':
            return HttpResponse('You have Authorize view this Page:')
        
    return wrapper_function