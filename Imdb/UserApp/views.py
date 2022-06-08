from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# from rest_framework_simplejwt.tokens import RefreshToken


from .serializer import User_Serializer
# Create your views here.
@api_view(['POST'],)
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
        

@api_view(['POST'],)
def registeration_view(request):
    if request.method == 'POST':
        data = {}
        serializer = User_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # refresh = RefreshToken.for_user(account)
            # data['token'] = {
            #             'refresh': str(refresh),
            #             'access': str(refresh.access_token),
            #         }
            return Response(serializer.data)
        
        
