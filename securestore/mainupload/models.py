from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from securestore.settings import MEDIA_ROOT

import os
import re
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


def content_file_name(instance, filename):
  #  print(ext)
    filename = "{}_{}_{}".format(
        instance.get_user().pk, instance.directory.pk, filename)
    fs = File.objects.filter(file=os.path.join('files', filename))
    ext = filename.split(".")[-1]
    res = "".join(filename.split(".")[:-1])
    files = [f for f in os.listdir(os.path.join(MEDIA_ROOT, 'files'))]
    l = [m for m in files if re.match(res+'\d?\.'+ext+'$', m)]
    l = len(l)
    if l > 0:
        filename = res + str(l) + "." + ext
    return os.path.join('files/', filename)


class File(models.Model):
    file = models.FileField(upload_to=content_file_name)
    protected = models.BooleanField(default=False)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    directory = GenericForeignKey('content_type', 'object_id')

    def get_user(self):
        dir = self.directory
        while not isinstance(dir, RootDirectory):
            dir = dir.parent

        return dir.User

    def name(self):
        return "".join(os.path.basename(self.file.name).split('_')[2:])
