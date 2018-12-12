from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
#from django.core.files.storage import fileSystemStorage
from .serializers import FileSerializer, DirectorySerializer, RootDirectorySerializer,  SubDirSerializer
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.views.decorators.csrf import csrf_exempt
from braces.views import CsrfExemptMixin
import json
from .models import Directory, RootDirectory

# Create your views here.


@csrf_exempt
def download_file(request):
    filepk = int(request.POST['fileid'])
    file = File.objects.get(pk=filepk)
    if file.get_user != request.user:
        HttpResponse("Unauthorizd", 401)
    wrapper = FileWrapper(file)
    response = HttpResponse(wrapper, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename={}'
    .format(file.name())
    response['Content-Length'] = os.path.getsize(filename)
    return response


def index(request):
    return HttpResponse('hi')


def create_file(request):
    parent_pk = request.POST['parent_pk']

    f = CreateFIle()

    parent.files.create(das)


@csrf_exempt
def create_directory(request):
    return HttpResponse(request.POST['folder_name'])


class FileView(CsrfExemptMixin, APIView):
    parser_classes = (MultiPartParser, FormParser)
    authentication_classes = []

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
        if user != request.user:
            return HttpResponse("401 Unauthorized", 401)
        serializer = serializer(parent)
        return Response(serializer.data)
