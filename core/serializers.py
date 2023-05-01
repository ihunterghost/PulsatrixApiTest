from rest_framework import serializers
from .models import log

class logSerializer(serializers.ModelSerializer):
    class Meta:
        model = log
        fields = ['id', 'mac', 'slave', 'message', 'created', 'updated']