from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('recent/', views.Recent, name="recent"),
    path('storage/', views.Storage, name="storage"),
    path('help/', views.Help, name="help"),
    path('contactus/', views.ContactUs, name="contactus"),
    path('aboutus/', views.AboutUs, name="aboutus"),
]
