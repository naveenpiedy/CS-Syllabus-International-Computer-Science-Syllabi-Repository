from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django import forms
from django.template.context_processors import csrf


def index(request):
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if "button_click" in request.POST:
            print(username, password)
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
            else:
                print("Debugging")
    return render(request, 'loginapp/base.html', c)

