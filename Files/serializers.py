from rest_framework import serializers
from .models import Files, TypeFile


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files
        fields = (
            'id',
            'name',
            'slug',
            'path',
            'type'
        )


class TypeFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeFile
        fields = (
            'id',
            'name'
        )
