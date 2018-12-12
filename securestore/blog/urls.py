from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url,include
app_name="blog"
urlpatterns = [
<<<<<<< HEAD

    path('', views.main_page,name='main_page'),
=======
    path('admin/', admin.site.urls),
    url('^#',include('django.contrib.auth.urls')),
    path('', views.main_page,name='main_page' ),
>>>>>>> 38972e3db27ed0c28014857a5b0ca62a536a1a76
]
