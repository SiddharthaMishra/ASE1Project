from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

# Create your models here.


class Photo(models.Model):
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='mainupload/')

class RootDirectory(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    children = GenericRelation('Directory', related_query_name='dirs')
    files = GenericRelation('File', related_query_name='all_files')


class Directory(models.Model):
    name = models.CharField(max_length=30)

    children = GenericRelation('self', related_query_name='dirs')
    files = GenericRelation('File', related_query_name='all_files')

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    parent = GenericForeignKey('content_type', 'object_id')

    def get_user(self):
        dir = self.directory
        while not isinstance(dir, RootDirectory):
            dir = dir.parent

        return dir.User

class File(models.Model):
    file = models.FileField(upload_to='files/')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    directory = GenericForeignKey('content_type', 'object_id')

    def get_user(self):
        dir = self.directory
        while not isinstance(dir, RootDirectory):
            dir = dir.parent

        return dir.User
