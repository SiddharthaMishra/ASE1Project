from django.shortcuts import render, redirect
from .models import UserFeedback
# Create your views here.

def feedback_index(request):
    if request.method == 'GET':
        return render(request, 'feedback/1.html')

def submit_feedback(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')
        if first_name and last_name and email and phone_number and message:
            feedback_obj = UserFeedback.objects.create()
            feedback_obj.first_name = first_name
            feedback_obj.last_name = last_name
            feedback_obj.email = email
            feedback_obj.phone = phone_number
            feedback_obj.message = message
            feedback_obj.save()
            return render(request, 'feedback/feedback_sent.html')
        else:
            redirect('/feedback_index/')
