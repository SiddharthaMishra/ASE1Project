from django.views.decorators.csrf import csrf_exempt
from django.urls import path
from .views import DirectoryView, get_filestring
from .views import FileView, index, share_file, get_storage, copy_file

urlpatterns = [
    path('', index),
    path('api/get_storage/', get_storage),
    path('api/procfile/', get_filestring),
    path('api/', DirectoryView.as_view()),
    path('api/<int:is_directory>/<int:pk>', DirectoryView.as_view()),
    path('api/files/', FileView.as_view()),
    path('api/share/', share_file),
    path('api/copy/', copy_file),
    path('api/<int:pk>/', FileView.as_view())
    # url(r'^api/uploader/$',markdown_uploader, name='markdown_uploader_page'),
]
