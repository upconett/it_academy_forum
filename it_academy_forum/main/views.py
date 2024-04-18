from django.http import *
from django.shortcuts import render, redirect

from .utility import *
from user.models import User


def redirector(request: HttpRequest):
    if request.method == 'GET':
        if not valid_cookies(request): return redirect('/login')
        return redirect('/home')

    return Http404()


def home(request: HttpRequest):
    if request.method == 'GET':
        if not valid_cookies(request): return redirect('/login')
        return render(request, 'main/home.html')
    return Http404()


def register(request: HttpRequest):
    if request.method == 'GET':
        return render(request, 'main/register.html', {'fail': failure(request)})
    elif request.method == 'POST':
        try:
            data = get_register_data(request)
            user = User.objects.create()
            response = HttpResponseRedirect('/home')
            set_user_cookies(user, response)
            return response
        except InvalidData: return render(request, 'main/register.html', fail_1_dict(request))
        except User.DoesNotExist: return redirect('/register?fail=1')
    return Http404()


def login(request: HttpRequest):
    if request.method == 'GET':
        return render(request, 'main/login.html', {'fail': failure(request)})
    elif request.method == 'POST':
        try:
            data = get_login_data(request)
            user = User.objects.get(**data)
            response = HttpResponseRedirect('/home')
            set_user_cookies(user, response)
            return response
        except InvalidData: return redirect('/login?fail=1')
        except User.DoesNotExist: return redirect('/login?fail=1')
        
    return Http404()

