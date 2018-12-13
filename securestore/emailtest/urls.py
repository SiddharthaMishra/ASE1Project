from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from login_signup import views
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.main,name='main'),
    url(r'^login_signup/',include('login_signup.urls')),
    url(r'^logout/$', views.user_logout, name='logout'),
    url('^',include('django.contrib.auth.urls')),
]
