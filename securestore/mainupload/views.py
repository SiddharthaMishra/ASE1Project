from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer, DirectorySerializer, RootDirectorySerializer,  SubDirSerializer
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.views.decorators.csrf import csrf_exempt
from braces.views import CsrfExemptMixin
import json
import os
from .models import Directory, RootDirectory, File, SharedFiles
from wsgiref.util import FileWrapper
from django.contrib.auth.models import User
from django.core.files.base import ContentFile

# Create your views here.


@csrf_exempt
def copy_file(request):
    file = File.objects.get(pk=request.POST['pk'])
    newfile = ContentFile(file.file.read())

    newfile.name = file.name()
    data = {
        'file': newfile,
        'protected': file.protected,
        'parent_is_root': True,
        'parent_pk': request.user.rootdirectory.pk
    }
    file_serializer = FileSerializer(data=data)
    if file_serializer.is_valid():
        file_serializer.save()
        return HttpResponse("done")
    else:
        return HttpResponse("notdone")


@csrf_exempt
def share_file(request):

    owner = request.user
    print(owner)
    shared_user = User.objects.get(username=request.POST['username'])
    file = File.objects.get(pk=request.POST['file_pk'])
  #  if file.get_user != owner:
  #      return HttpResponse("Unauthorized", 401)
    s = SharedFiles.objects.create(File=file, User=shared_user)
    print(s)
    return HttpResponse("")


@csrf_exempt
def index(request):
    return HttpResponse(request.user.username)


class FileView(CsrfExemptMixin, APIView):
    authentication_classes = []
    parser_classes = (MultiPartParser, FormParser)

    def delete(self, request, pk):
        print(request.user)
        f = File.objects.get(pk=pk)
#        if f.get_user() != request.user:
#            return HttpResponse("Unauthorized", 401)
        f.delete()
        return HttpResponse("")

    def get(self, request, pk):
        file = File.objects.get(pk=pk)
        print(file.get_user(), request.user)

#        if file.get_user() != request.user:
 #           return HttpResponse("Unauthorized", 401)

        wrapper = FileWrapper(file.file)
        response = HttpResponse(
            file.file.read(), content_type='application/force-download')
        response['Content-Disposition'] = 'attachment; filename={}'.format(
            file.name())
        response['Content-Length'] = os.path.getsize(file.file.path)
        return response

    def post(self, request):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data,
                            status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class DirectoryView(CsrfExemptMixin, APIView):
    authentication_classes = []

    def post(self, request):
        directory_serializer = DirectorySerializer(data=request.data)
        if directory_serializer.is_valid():
            directory_serializer.save()
            return Response(directory_serializer.data,
                            status=status.HTTP_201_CREATED)
        else:
            return Response(directory_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, is_directory, pk):
        if is_directory == 0:
            parent = RootDirectory.objects.get(pk=pk)
            serializer = RootDirectorySerializer
            user = parent.user
        else:
            parent = Directory.objects.get(pk=pk)
            serializer = DirectorySerializer
            user = parent.get_user()
#        if user != request.user:
#            return HttpResponse("401 Unauthorized", 401)
        serializer = serializer(parent)
       # console.log("hi")
       # console.log(Response(serializer.data))
        return Response(serializer.data)
