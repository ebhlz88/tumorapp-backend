from rest_framework import serializers
from .models import cameraimage


class CimageSerializer(serializers.ModelSerializer):
    class Meta:
        model = cameraimage
        fields = '__all__'