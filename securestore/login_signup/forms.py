from django import forms
from django.contrib.auth.models import User
class UserForm(forms.ModelForm):
    username = forms.CharField(min_length=6,max_length=100)
    email = forms.EmailField(max_length=200)
    password = forms.CharField(min_length=6,widget=forms.PasswordInput())
    confirm_password = forms.CharField(min_length=6,widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')
