from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

# Create your models here.


class RootDirectory(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    children = GenericRelation('Directory')


class Directory(models.Model):
    name = models.CharField(max_length=30)

    children = GenericRelation('self')

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    parent = GenericForeignKey('content_type', 'object_id')


class File(models.Model):
    file = models.FileField(upload_to='files/')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    directory = GenericForeignKey('content_type', 'object_id')
