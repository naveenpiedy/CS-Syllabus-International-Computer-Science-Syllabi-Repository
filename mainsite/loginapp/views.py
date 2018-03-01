from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django import forms
from django.template.context_processors import csrf
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from .tokens import password_reset_token
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.http import HttpResponse


def index(request):
    c = {}
    c.update(csrf(request))
    print(c)
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

def forget_password_step1(request):
    c = {}
    c.update(csrf(request))
    return render(request,'loginapp/step1.html',c)

def forget_password_step2(request):
    if request.method=='POST' and "button_click" in request.POST:
        email=request.POST['email']
        current_site = get_current_site(request)
        message = render_to_string('loginapp/reset_email.html', {
            'domain': current_site.domain,
            'token': password_reset_token.make_token(),
        })
        mail_subject = 'Activate your account.'
        to_email = email
        email_obj = EmailMessage(mail_subject, message, to=[to_email])
        email_obj.send()
        return HttpResponse('Please confirm your email address to complete the registration')
    return render(request,'')