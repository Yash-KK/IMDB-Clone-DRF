from django.contrib.auth.models import User
from rest_framework import serializers


class User_Serializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, style={'input_type': 'password'})
    class Meta:
        model = User
        fields = ['username','email','password','password2']
    
    def save(self):
        p1 = self.validated_data['password']
        p2 = self.validated_data['password2']
        if p1 != p2:
            raise serializers.ValidationError({"Error":"P1 and P2 are not the Same!!"})
        
        if User.objects.filter(email=self.validated_data['email']).exists():    
            raise serializers.ValidationError({"Error:":"User with email already exists!"})
        
        account = User.objects.create(username=self.validated_data['username'],email=self.validated_data['email'])
        account.set_password(p1)
        account.save()
        return account