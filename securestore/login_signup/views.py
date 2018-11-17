from django.shortcuts import render,redirect
from login_signup.forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from .models import UserData
import requests

#from django.contrib.auth.decorators import login_required


def main(request):
    return render(request,'login_signup/main.html')
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('main'))
def signup(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.is_active=False
            user.set_password(user.password)
            user.save()
            registered = True
            current_site = get_current_site(request)
            domain=current_site.domain
            print(domain)
            message = render_to_string('acc_active_email.html', {
                'user':user,
                'domain':current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
            to_email = user_form.cleaned_data.get('email')
            name= user_form.cleaned_data.get('username')
            password=user_form.cleaned_data.get('password')
            print(name)
            print(password)
            response = requests.get("http://api.quickemailverification.com/v1/verify?email="+to_email+"&apikey=519847e067dab09cd0a1c56e334105fffa8dd9793a96ccc61c808db1ae7f")
            result=response.json()

            if (result['did_you_mean']=='' and result['result']=="valid"):
                print("valid")
                userdata=UserData.objects.create(email=to_email,name=name,password=password)
                userdata.save()
                mail_subject = 'Activate your blog account.'
                to_email = user_form.cleaned_data.get('email')
                email = EmailMessage(mail_subject, message, to=[to_email])
                email.send()
                return HttpResponse("Please click on the link sent to your mail to activate your account")

            else:
                try:
                    u=User.objects.get(username=name)
                    u.delete()
                except User.DoesNotExist:
                    return HttpResponse('The email given is invalid please check it ')
                except Exception as e:
                    return render(request,'login_signup/signup.html',{'user_form':user_form})
                return HttpResponse('The email given is invalid please check it ')


        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request,'login_signup/signup.html',{'user_form':user_form,'registered':registered})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        # login(request, user)
        # return redirect('home')
        return render(request,'login_signup/login.html',{})
        # return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
        # return render(request, 'login.html', {'form': form})
    else:
        return HttpResponse('Activation link is invalid!')



def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('main'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'login_signup/login.html', {})
