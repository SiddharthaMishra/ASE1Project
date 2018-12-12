from django.urls import path
from .views import DirectoryView, FileView, index, share_file
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', index),
    path('api/', DirectoryView.as_view()),
    path('api/<int:is_directory>/<int:pk>', DirectoryView.as_view()),
    path('api/files/', FileView.as_view()),
    path('api/share/', share_file),
    path('api/<int:pk>/', FileView.as_view())
    # url(r'^api/uploader/$',markdown_uploader, name='markdown_uploader_page'),
]
