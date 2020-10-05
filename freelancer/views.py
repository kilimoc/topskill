from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage, send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from freelancer.token import account_activation_link
from topskill import settings


def registerFreelancer(request):
    if request.method == 'POST':
        fname=request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['cpassword']

        if password != confirm_password:
            messages.error(request,'Your Password do not match.Kindly enter matching Password')
        else:
            #Registration
            userO=User()
            userO.first_name=fname
            userO.last_name=lname
            userO.email=email
            userO.password=make_password(password,salt=None)
            userO.is_active=False
            userO.save()
            current_site=get_current_site(request)
            mail_subject='Activate Your TopSkill Account'
            message=render_to_string('acc_active_email.html',{
                'user':userO,
                'domain':current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(userO.pk)),
                'token':account_activation_link.make_token(userO)

            })
            to_email=email
            mailO=EmailMessage(mail_subject,message,settings.EMAIL_HOST_USER,to=[to_email])
            mailO.send(fail_silently=False)


            #Sending email address.
            return redirect('design:verificationsent')


    return render(request,'freelancer_signup.html')
def activate_account(request,uid64,token):
    try:
        uid=force_bytes(urlsafe_base64_encode(uid64))
        user=User.objects.get(pk=uid)

    except(TypeError,ValueError,OverflowError,User.DoesNotExist):
        user=None
    if user is not None and account_activation_link.check_token(user,token):
        user.is_active=True
        user.save()
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')
