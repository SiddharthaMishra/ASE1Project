from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from django.contrib import messages
from DispFile.forms import UserForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm

# Create your views here.


@csrf_exempt
class IndexView(DetailView):
    model = User

    template_name = 'LoginHome.html'


@login_required
def home(request):
    user = request.user
    context = {user: user}
    return render(request, 'LoginHome.html', context=context)


@login_required
def Help(request):
    return render(request, 'LoginHelp.html')


@login_required
def AboutUs(request):
    return render(request, 'LoginAboutUs.html')


@login_required
def ContactUs(request):
    return render(request, 'LoginContactUs.html')


@login_required
def viewprofile(request):
    args = {'user': request.user}

    return render(request, 'viewprofile.html', args)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()

            messages.success(
                request, ('Your profile was successfully updated!'))

            return redirect('DispFile:viewprofile')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)

    return render(request, 'edit_profile.html', {
        'user_form': user_form,

    })


@login_required
def change_password(request):

    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Imp
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('DispFile:viewprofile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })
