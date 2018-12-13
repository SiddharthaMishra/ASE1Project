from django.test import TestCase,Client
from .models import UserData
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
        form = UserForm(data={ 'username': 'someone','email': 'someone@gmail.com', 'password': 'user@12345','confirm_password':'user@12345'})
        self.assertTrue(form.is_valid())

    def test_UserForm_is_invalid(self):
        form = UserForm(data={'email': "user@mp.com", 'password': ""})
        self.assertFalse(form.is_valid())

    def test_UserForm_is_invalid2(self):
        form = UserForm(data={ 'password': ""})
        self.assertFalse(form.is_valid())

    def test_UserForm_is_empty(self):
        form = UserForm(data={ })
        self.assertFalse(form.is_valid())

class Url_Test(TestCase):

    def test_signup_url(self):
        response = self.client.get("/signup/")
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'login_signup/signup.html')

    def test_login_url(self):
        response = self.client.get("/login")
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'login_signup/login.html')

    def test_login_wrong_url(self):
        response = self.client.get("/logi")
        self.assertEqual(response.status_code,404)

    def test_user_logout_worn_url(self):
        response = self.client.get("/log")
        self.assertEqual(response.status_code,404)

    def test_user_logout_url(self):
        response =  self.client.get("/logout/")
        self.assertEqual(response.status_code,302)

    def test_user_logout_url_by_name(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code,302)


class Views_test(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user('Bean2',password='something123',email='something1234@gmail.com')
        UserData.objects.create(name='Bean2',password='something123',email='something1234@gmail.com')

    def test_login_details(self):
        login=self.client.login(username="Bean2",password="something123")
        self.assertEqual(login,True)
        response = self.client.get(reverse("login"))
        self.assertEqual(str(response.context['user']), 'Bean2')
        self.assertEqual(response.status_code,200)

    def test_login_redirect(self):
        login=self.client.login(username="Bean2",password="something123")
        self.assertEqual(login,True)
        response = self.client.get("/")
        self.assertEqual(response.status_code,302)

    def test_signup_view(self):
        response = self.client.get("/signup/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "login_signup/signup.html")

    def test_login_view(self):
        response = self.client.get("/login/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "login_signup/login.html")

    def test_adding_user(self):
        user_count = User.objects.count()
        response = self.client.post(reverse("login_signup:signup"), {'email': "somanarupesh32@gmail.com", 'password': "qwerty", 'username': "user123",'confirm_password ' :"qwerty",})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.count(), user_count+1)

    def test_adding_user_invalid_details(self):
        user_count = User.objects.count()
        response = self.client.post(reverse("login_signup:signup"), {'email': "somanarupesh32@gmail.com", 'password': "", 'username': "",'confirm_password ' :"",})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.count(), user_count)

class Login_required_Test(TestCase):

    def test_redirect_if_not_logged_in(self):
        self.client.logout()
        response = self.client.get(reverse('DispFile:help'))
        self.assertRedirects(response, '/help/login/?next=/help/')

    def test_redirect_if_not_logged_in_2(self):
        self.client.logout()
        response = self.client.get(reverse('DispFile:contactus'))
        self.assertRedirects(response, '/contactus/login/?next=/contactus/')

    def test_redirect_if_not_logged_in_3(self):
        self.client.logout()
        response = self.client.get(reverse('DispFile:viewprofile'))
        self.assertRedirects(response, '/viewprofile/login/?next=/viewprofile/')

    def test_redirect_if_not_logged_in_4(self):
        self.client.logout()
        response = self.client.get(reverse('DispFile:editprofile'))
        self.assertRedirects(response, '/viewprofile/editprofile/login/?next=/viewprofile/editprofile/')

    def test_redirect_if_not_logged_in_5(self):
        self.client.logout()
        response = self.client.get(reverse('DispFile:change_password'))
        self.assertRedirects(response, '/viewprofile/password/login/?next=/viewprofile/password/')
