from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'LoginHome.html')


def Recent(request):
    return render(request,'LoginRecent.html')

def Storage(request):
    return render(request,'LoginStorage.html')

def Help(request):
    return render(request,'LoginHelp.html')

def AboutUs(request):
    return render(request,'LoginAboutUs.html')

def ContactUs(request):
    return render(request,'LoginContactUs.html')
