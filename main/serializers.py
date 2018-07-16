from rest_framework import serializers
from . import models

class MainSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Main
        fields = '__all__'
