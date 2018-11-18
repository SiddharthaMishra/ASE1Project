from django.conf.urls import url

from login_signup import views
from django.urls import path, re_path
import DispFile.views

app_name = 'login_signup'
urlpatterns = [
    path('home', DispFile.views.home, name='home'),
    url('signup/', views.signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    url('login', views.user_login, name='user_login'),
    url(
        r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),

]
