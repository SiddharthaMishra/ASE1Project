from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
  user = models.OneToOneField(User,on_delete=models.CASCADE)
def __str__(self):
  return self.user.username

class UserData(models.Model):
    email = models.EmailField(max_length=200, help_text='Required')
    name = models.CharField(max_length=200)
    password= models.CharField(max_length=200)
