from rest_framework import serializers
from .models import Movie

class Movie_Serializer(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields = '__all__'
        
    def get_len_name(self,obj):
        return len(obj.movie)
        


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
    
    
    
                