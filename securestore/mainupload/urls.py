from django.urls import path
from .views import index, DirectoryView, create_directory, FileView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', index),
    path('create/', create_directory),
    path('api/', DirectoryView.as_view()),
    path('api/<int:is_directory>/<int:pk>', DirectoryView.as_view()),
    path('api/files/',FileView.as_view()),
    # url(r'^api/uploader/$',markdown_uploader, name='markdown_uploader_page'),
]
