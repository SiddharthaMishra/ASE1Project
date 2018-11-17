from django.conf.urls import url

from login_signup import views
from django.urls import path,re_path

app_name = 'login_signup'
urlpatterns=[
    path('',views.signup,name='signup'),
    path('',views.main,name='main'),
    url('login_signup/signup.html/',views.signup,name='signup'),
    url('login_signup/login.html',views.user_login,name='user_login'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate , name='activate'),

]
