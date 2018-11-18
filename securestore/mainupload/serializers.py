from rest_framework import serializers

from .models import Directory, File, RootDirectory


class FileSerializer(serializers.ModelSerializer):
    file = serializers.FileField(use_url=False)

    class Meta:
        model = File
        fields = ('file', 'pk')

    def create(self, validated_data):
        pass


class SubDirSerializer(serializers.ModelSerializer):
    class Meta:
        model = Directory
        fields = ('name', 'pk')


class ParentDirSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    is_root = serializers.SerializerMethodField()

    def get_is_root(self, obj):
        return isinstance(obj, RootDirectory)


class DirectorySerializer(serializers.ModelSerializer):
    parent = ParentDirSerializer()
    files = FileSerializer(many=True)
    children = SubDirSerializer(many=True)

    class Meta:
        model = Directory
        fields = ('name', 'parent', 'files', 'children')
        depth = 1

    def create(self, validate_data):
        Directory.objects.create()


class RootDirectorySerializer(serializers.ModelSerializer):
    files = FileSerializer(many=True)
    children = SubDirSerializer(many=True)

    class Meta:
        model = RootDirectory
        fields = ('name', 'files', 'children')
