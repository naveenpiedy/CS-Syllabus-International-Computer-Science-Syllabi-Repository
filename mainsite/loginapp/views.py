from django.shortcuts import render, redirect
from django.contrib.auth.models import User
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
    if request.method=='POST' and "button_click" in request.POST:
        get_email=request.POST['email']
        users=User.objects.filter(email=get_email)
        list_id=[]
        for user in users:
            list_id.append(user.id)
        max_id=max(list_id)
        spec_user=User.objects.get(id=max_id)
        print(type(spec_user))
        current_site = get_current_site(request)
        message = render_to_string('loginapp/email.html', {
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(spec_user.pk)),
            'token': password_reset_token.make_token(user),
        })
        mail_subject = 'Reset your password.'
        to_email = get_email
        email_obj = EmailMessage(mail_subject, message, to=[to_email])
        email_obj.send()
        return HttpResponse('Please confirm your email address to complete the password reset')
    return render(request,'loginapp/step1.html',c)

def reset(request, uidb64, token):
    g=uidb64[1:]
    g = g.replace('\'','')
    uid = force_text(urlsafe_base64_decode(str(g)))
    print(uid)
    try:
        uid = force_text(urlsafe_base64_decode(uidb64[1:].replace('\'','')))
        print(uid)
        user = User.objects.get(pk=uid)
        print(uidb64)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and password_reset_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return render(request,'loginapp/passwordReset.html')
    else:
        return HttpResponse("THHH")