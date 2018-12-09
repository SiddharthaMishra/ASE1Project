from django.urls import path, include
from . import views
app_name= 'DispFile'
urlpatterns = [
    path('',views.home,name="home"),
    path('help/',views.Help,name="help"),
    path('contactus/',views.ContactUs,name="contactus"),
    path('aboutus/',views.AboutUs,name="aboutus"),
]
