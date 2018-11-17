
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='blog-home' ),
    path('index.html/', views.homes,name='blog-homes' ),
]