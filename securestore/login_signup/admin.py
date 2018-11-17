
# Register your models here.
from django.contrib import admin
from login_signup.models import UserProfileInfo, User
from .models import UserData

admin.site.register(UserData)
# Register your models here.
admin.site.register(UserProfileInfo)
