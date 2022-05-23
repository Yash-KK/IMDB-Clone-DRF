from rest_framework import serializers


class Movie_Serializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    movie = serializers.CharField()
    description = serializers.CharField()
    is_active = serializers.BooleanField(default=True)
        