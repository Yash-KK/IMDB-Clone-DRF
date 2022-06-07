from rest_framework import serializers
from .models import (
    WatchList,
    StreamPlatform,
    Review
    )

class Review_Serializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        # fields = '__all__'
        exclude = ('watchlist',)

    
    
class WatchList_Serializer(serializers.ModelSerializer):
    reviews = Review_Serializer(read_only=True,many=True)
    
    class Meta:
        model = WatchList
        fields = '__all__'
    
    
        
        
class StreamPlatform_Serializer(serializers.ModelSerializer):
    watchlist = WatchList_Serializer(many=True,read_only=True)
    class Meta:
        model = StreamPlatform
        fields = '__all__'
        
   
        


# class Movie_Serializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     movie = serializers.CharField()
#     description = serializers.CharField()
#     is_active = serializers.BooleanField(default=True)
    
#     def create(self, validated_data):       
#        return Movie.objects.create(**validated_data)
    
    
#     def update(self, instance, validated_data):       
#         instance.movie = validated_data.get('movie', instance.movie)
#         instance.description = validated_data.get('description', instance.description)
#         instance.is_active = validated_data.get('is_active', instance.is_active)        
#         instance.save()
#         return instance    
    
#     def validate(self, data):
#         """
#         Check that start is before finish.
#         """
#         if data['movie'] == data['description']:
#             raise serializers.ValidationError("Movie and Description must not be the Same!")
#         return data
    
#     def validate_movie(self,value):
#         if len(value)<2:
#             raise serializers.ValidationError("Length is Too Short!")
#         return value
    
    
    
