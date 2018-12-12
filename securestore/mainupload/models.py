from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from securestore.settings import MEDIA_ROOT
from django.utils import timezone
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

import datetime
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
        dir = self.parent
        while not isinstance(dir, RootDirectory):
            dir = dir.parent

        return dir.User


def content_file_name(instance, filename):
  #  print(ext)
    filename = "{}_{}_{}".format(
        instance.get_user().pk, instance.directory.pk, filename)
    files = os.listdir(os.path.join(MEDIA_ROOT, 'files'))
    if filename in files:
        fs = File.objects.filter(file=os.path.join('files', filename))
        ext = filename.split(".")[-1]
        res = "".join(filename.split(".")[:-1])
        l = [m for m in files if re.match(res+'\d?\.'+ext+'$', m)]
        l = len(l)
        filename = res + str(l) + "." + ext
    return os.path.join('files/', filename)


class File(models.Model):

    file = models.FileField(upload_to=content_file_name)
    protected = models.BooleanField(default=False)
    uploaded = models.TimeField(default=timezone.now)

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


class SharedFiles(models.Model):
    File = models.ForeignKey(File, on_delete=models.CASCADE)
    User = models.ForeignKey(User, on_delete=models.CASCADE)


def _delete_file(path):
    # Deletes file from filesystem.
    if os.path.isfile(path):
        os.remove(path)


@receiver(pre_delete, sender=File)
def delete_img_pre_delete_post(sender, instance, *args, **kwargs):
    if instance.file:
        _delete_file(instance.file.path)
