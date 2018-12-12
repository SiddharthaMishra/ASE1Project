from django.test import TestCase
from rest_framework.test import RequestsClient
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import Directory , File,RootDirectory
from rest_framework.test import APIRequestFactory
import json
from .views import *
# Create your tests here.
client = RequestsClient()
factory = APIRequestFactory()


class Rest_framework_tests(APITestCase):



    def test_create_directory(self):
        url = "http://127.0.0.1:8000/mainupload/api"
        data ={'name':'test','parent_id':'1','parent_is_root':'false'}
        response = self.client.post(url,data,format="json")
        print(RootDirectory.objects.all())
        self.assertEqual(response.status_code, 200)

    def test_get_data(self):
        view = DirectoryView.as_view()
        url = "mainupload/api/4/2"
        request = factory.get(url)
        response = view(request, pk="1",is_directory="1")
        response.render()
        print(response.content)
        self.assertEqual(json.loads(response.content),{"pk":2,"name":"asdasd","files":[],"children":[{"name":"newer","pk":35}]})
