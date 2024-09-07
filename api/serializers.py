from rest_framework import serializers
from .models import ShortLink

class ShortLinkSerializer():

    class RetrivalSerializer(serializers.ModelSerializer):
        class Meta:
            model = ShortLink
            fields = ['id', 'short_code', 'url', 'createdAt', 'updatedAt']

    class StatsSerializer(serializers.ModelSerializer):
        class Meta:
            model = ShortLink
            fields = ['id', 'short_code', 'url', 'createdAt', 'updatedAt', 'accessCount']