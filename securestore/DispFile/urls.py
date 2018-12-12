from django.urls import path, include
from . import views
app_name= 'DispFile'
urlpatterns = [
    path('',views.home,name="home"),
    path('help/',views.Help,name="help"),
    path('contactus/',views.ContactUs,name="contactus"),
    path('aboutus/',views.AboutUs,name="aboutus"),
    path('viewprofile/',views.viewprofile,name="viewprofile"),
    path('viewprofile/editprofile/',views.edit_profile,name="editprofile"),
    path('viewprofile/password/', views.change_password, name='change_password'),
    path('recent/', views.recent, name="Recent"),
    path('sharedwithme/', views.sharedwithme, name="sharedwithme"),

]
