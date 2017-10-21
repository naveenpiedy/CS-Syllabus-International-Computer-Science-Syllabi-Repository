from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import authenticate
from django import forms
from django.template.context_processors import csrf
from registration.forms import RegistrationForm


def index(request):
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        print(request.POST)
        username = request.POST['user_name']
        if request.POST['pwd'] == request.POST['re_pwd']:
            password = request.POST['pwd']
        else:
            raise "Password doesn't match"
        if request.POST['email_id'] == request.POST['re_email_id']:
            email = request.POST['email_id']
        else:
            raise "Email ID doesn't matach"
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        print(username, password)
        if "button_click" in request.POST:
            print(username, password)
            user = User.objects.create_user(username= username, password= password, email=email)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
    return render(request, 'signupapp/SER517Login.html', c)

