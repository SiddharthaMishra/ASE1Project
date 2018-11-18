from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect, reverse

def home(request):
    if request.user.is_authenticated:
        return redirect(reverse("login_signup:home"))
    return render(request,'index.html')
