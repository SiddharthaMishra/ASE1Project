from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url,include
app_name="blog"
urlpatterns = [
    path('admin/', admin.site.urls),
    url('^#',include('django.contrib.auth.urls')),
    path('', views.main_page,name='main_page' ),
]
