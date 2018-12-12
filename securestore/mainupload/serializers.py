from rest_framework import serializers
import json

from .models import Directory, File, RootDirectory


class FileSerializer(serializers.ModelSerializer):
    file = serializers.FileField(use_url=False, write_only=True)
    parent_pk = serializers.IntegerField(write_only=True)
    parent_is_root = serializers.BooleanField(write_only=True)
    #name = serializers.SerializerMethodField()
    class Meta:
        model = File
        fields = ('file', 'protected', 'name', 'pk', 'parent_pk', 'parent_is_root')
        read_only_fields = ('pk',)

    def create(self, validated_data):
        if validated_data['parent_is_root']:
            parent = RootDirectory
        else:
            parent = Directory

        parent = parent.objects.get(pk=validated_data['parent_pk'])
        f = parent.files.create(file=validated_data['file'], 
                protected=validated_data['protected'])
        return f

class SubDirSerializer(serializers.ModelSerializer):
    class Meta:
        model = Directory
        fields = ('name', 'pk')


class ParentDirSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    root = serializers.SerializerMethodField()
    is_root = serializers.BooleanField(write_only=True)

    def get_root(self, obj):
        return isinstance(obj, RootDirectory)


class DirectorySerializer(serializers.ModelSerializer):
    files = FileSerializer(many=True, required=False)
    children = SubDirSerializer(many=True, required=False)
    #parent = ParentDirSerializer()
    parent_id = serializers.IntegerField(write_only=True)
    parent_is_root = serializers.BooleanField(write_only=True)

    class Meta:
        model = Directory
        fields = ('pk','name',  'parent_id', 'parent_is_root', 'files', 'children')
        read_only_fields = ('files', 'children','pk')
        depth = 1

    def create(self, validated_data):
        if validated_data['parent_is_root']:
            parent = RootDirectory
        else:
            parent = Directory

        parent = parent.objects.get(pk=int(validated_data['parent_id']))

        return Directory.objects.create(parent=parent, name=validated_data['name'])


class RootDirectorySerializer(serializers.ModelSerializer):
    files = FileSerializer(many=True, required=False)
    children = SubDirSerializer(many=True, required=False)

    class Meta:
        model = RootDirectory
        fields = ('files', 'children')
        depth = 0
