from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render
from django.template.context_processors import csrf
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from .tokens import account_activation_token


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
            user.is_active = False
            user.save()
        current_site = get_current_site(request)
        message = render_to_string('signupapp/email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        mail_subject = 'Activate your account.'
        to_email = email
        email = EmailMessage(mail_subject, message, to=[to_email])
        email.send()
        return HttpResponse('Please confirm your email address to complete the registration')
    return render(request, 'signupapp/SER517Login.html', c)

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

