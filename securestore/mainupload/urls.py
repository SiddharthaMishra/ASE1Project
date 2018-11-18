from django.urls import path
from .views import index, DirectoryView

urlpatterns = [
    path('', index),
    path('api/', DirectoryView.as_view()),
]
