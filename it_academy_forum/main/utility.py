from django.http import *

from user.models import User


class InvalidData(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

        
def failure(request: HttpRequest):
    return request.GET.get('fail', 0)


def valid_cookies(request: HttpRequest):
    email = request.get_signed_cookie('email', None)
    password = request.get_signed_cookie('password', None)
    return all([email, password])


def get_login_data(request: HttpRequest):
    data = {}
    data['email'] = request.POST.get('email', None)
    data['password'] = request.POST.get('password', None)
    if not all(data.values()): raise InvalidData('Login')
    return data


def get_register_data(request: HttpRequest):
    data = {}
    data['email'] = request.POST.get('email', None)
    data['password'] = request.POST.get('password', None)
    if not all(data.values()): raise InvalidData('Login')
    return data


def set_user_cookies(user: User, response: HttpResponse):
    response.set_signed_cookie('username', user.username)
    response.set_signed_cookie('email', user.email)
    response.set_signed_cookie('password', user.password)


def fail_1_dict(request: HttpRequest) -> dict:
    return {
        'fail': 'Вы ввели не все данные!',
        'username': request.POST.get('username'),
        'email': request['email'],
        'password': request['password'],
    }


def fail_2_dict(data: dict) -> dict:
    return {
        'fail': 'Неверный логин или пароль!',
        'username': data['username'] if 'username' in data.keys() else None,
        'email': data['email'],
        'password': data['password'],
    }

    