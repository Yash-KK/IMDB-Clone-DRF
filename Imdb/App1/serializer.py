from rest_framework import serializers
from .models import Movie

class Movie_Serializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    movie = serializers.CharField()
    description = serializers.CharField()
    is_active = serializers.BooleanField(default=True)
    
    def create(self, validated_data):       
       return Movie.objects.create(**validated_data)
    
    def update(self, instance, validated_data):       
        instance.movie = validated_data.get('movie', instance.movie)
        instance.description = validated_data.get('description', instance.description)
        instance.is_active = validated_data.get('is_active', instance.is_active)        
        instance.save()
        return instance    