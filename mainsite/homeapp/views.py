from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from signupapp.models import UserTable


# def index(request):
#     return render(request, 'homeapp/dashboard.html')

def index(request):
    First_Name = ""
    Last_Name = ""
    Email = ""
    Username = ""
    University = ""
    IsPro = ""
    usertable = UserTable()
    #if request.method == 'POST':
    if request.user.is_authenticated:
        First_Name = request.user.first_name
        Last_Name = request.user.last_name
        Email = request.user.email
        Username = request.user.username
        University = request.user.userinfo.university
        IsPro = request.user.userinfo.isprofessor
    return render(request, 'homeapp/dashboard.html', {
        'First_Name': First_Name, 'Last_Name' : Last_Name, 'Email_Address' : Email, 'Username' : Username,
        'University' : University, 'Isprofessor' : IsPro
    })