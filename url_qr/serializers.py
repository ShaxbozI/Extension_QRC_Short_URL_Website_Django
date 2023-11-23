import django.core.validators
from rest_framework import serializers
from .models import Url_QR


class UrlQrSerializer(serializers.ModelSerializer):
    generate = serializers.BooleanField(default = False)
    select_1 = serializers.CharField(max_length = 1, allow_blank=True)
    select_2 = serializers.CharField(max_length = 1, allow_blank=True)
    # url_shorted = serializers.CharField(max_length = 10, allow_blank=True)
    
    class Meta:
        model = Url_QR
        fields = (
            'url_long',
            'url_short',
            'generate',
            'select_1',
            'select_2',
        )