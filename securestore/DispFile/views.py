from django.shortcuts import render

from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView

# Create your views here.


class IndexView(DetailView):
    model = User

    template_name = 'LoginHome.html'


@login_required
def home(request):
    user = request.user
    context = {user: user}
    return render(request, 'LoginHome.html', context=context)


def Recent(request):
    return render(request, 'LoginRecent.html')


def Storage(request):
    return render(request, 'LoginStorage.html')


def Help(request):
    return render(request, 'LoginHelp.html')


def AboutUs(request):
    return render(request, 'LoginAboutUs.html')


def ContactUs(request):
    return render(request, 'LoginContactUs.html')