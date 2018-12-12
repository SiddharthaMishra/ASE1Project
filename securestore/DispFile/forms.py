from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=300, help_text='Required')
   
    class Meta():
        model = User
        fields = ('username','email')


    def save(self, user=None):
        user_profile=super(UserForm, self).save(commit=False)
        if user:
            user_profile.user=user
        user_profile.save()
        return user_profile 