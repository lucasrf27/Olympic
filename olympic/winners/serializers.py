from .models import *
from rest_framework import serializers




class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'name', 'sex', 'age', 'height', 'weight', 'team']