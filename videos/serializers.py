from rest_framework import serializers


class VideoSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
    href = serializers.URLField()
    post_date = serializers.DateField()
    views_count = serializers.IntegerField()
