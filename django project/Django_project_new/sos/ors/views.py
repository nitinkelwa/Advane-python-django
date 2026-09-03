from django.shortcuts import render
from django.template.context_processors import request

from .service.user_service import UserService


def welcome(request):
    return render(request, 'welcome.html')


def user_signup(request):
    if request.method == "POST":
        form = {}
        form['first_name'] = request.POST.get('firstName')
        form['last_name'] = request.POST.get('lastName')
        form['login_id'] = request.POST.get('loginId')
        form['password'] = request.POST.get('password')
        form['dob'] = request.POST.get('dob')
        form['address'] = request.POST.get('address')

        service = UserService()
        service.add(form)

    return render(request, 'registration.html')


def user_signin(request):
    message = ''
    if request.method == "POST":
        form = {}
        form['login_id'] = request.POST.get('loginId')
        form['password'] = request.POST.get('password')

        service = UserService()
        records = service.authenticate(form['login_id'], form['password'])

        if len(records) > 0:
            return render(request, 'welcome.html', {'firstName': records[0].get('first_name')})
        else:
            message = 'LoginId & Password Invalid'

    return render(request, 'login.html', {'message': message})
