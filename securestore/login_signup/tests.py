from django.test import TestCase,Client
from .models import UserProfileInfo,UserData
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import *
from DispFile.views import *
client=Client()
# Create your tests here.

class User_Profile_Model_Test(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user('Bean2',password='something123',email='something1234@gmail.com')
        UserData.objects.create(name='Bean2',password='something123',email='something1234@gmail.com')

    def test_username(self):
        userid=len(UserData.objects.all())
        user=UserData.objects.get(id=userid)
        # field_label = author._meta.get_field('name').verbose_name
        self.assertEquals(user.name,'Bean2')

    def test_UserEmail(self):
        userid=len(UserData.objects.all())
        user=UserData.objects.get(id=userid)
        self.assertEquals(user.email,'something1234@gmail.com')

    def checkUserIsNotSuperUser(self):
        user=User.objects.get(username="Bean2")
        self.assertEquals(user.is_superuser,False)


# class EmailVerificationApiTest(TestCase):
class User_Form_Test(TestCase):

    def test_UserForm_is_valid(self):
        form = UserForm(data={ 'username': "someone",'email': "someone@gmail.com", 'password': "user@12345"})
        self.assertTrue(form.is_valid())

    def test_UserForm_is_invalid(self):
        form = UserForm(data={'email': "user@mp.com", 'password': ""})
        self.assertFalse(form.is_valid())

class Views_Test(TestCase):

    def test_signup_view(self):
        response = self.client.get("/signup/")
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'login_signup/signup.html')

    def test_login_view(self):
        response = self.client.get("/login")
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'login_signup/login.html')


    def test_user_logout_view(self):
        response =  self.client.get("/logout/")
        self.assertEqual(response.status_code,302)

    # def test_redirect_if_not_logged_in(self):
    #     self.client.logout()
    #     response = self.client.get(reverse('Help'))
    #     self.assertRedirects(response, '/help/login/?next=/help/')
