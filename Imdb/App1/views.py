from django.http import HttpResponse
from django.shortcuts import render

from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status

from .serializer import (
    WatchList_Serializer,
    StreamPlatform_Serializer
    
)
from .models import (
    WatchList,
    StreamPlatform
)

# Create your views here.
"""
Watch List related
"""
class WatchListAPV(APIView):
    def get(self,request):
        watchlist = WatchList.objects.all()
        serializer = WatchList_Serializer(watchlist,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = WatchList_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)            

class WatchDetailAPV(APIView):
    def get(self,request,id):
        try:
            watchlist = WatchList.objects.get(pk=id)
        except WatchList.DoesNotExist:
            return Response({"error":"Not Found!"},status=status.HTTP_400_BAD_REQUEST)    
        serializer = WatchList_Serializer(watchlist)
        return Response(serializer.data)
        
    def put(self,request,id):
        watchlist = WatchList.objects.get(pk=id)
        serializer = WatchList_Serializer(watchlist,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)                
        
    def delete(self,request,id):
        watchlist = WatchList.objects.get(pk=id)
        watchlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    

"""Stream Platform related"""    
class StreamListAPV(APIView):
    def get(self,request):
        platforms = StreamPlatform.objects.all()
        serializer = StreamPlatform_Serializer(platforms,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = StreamPlatform_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
class StreamDetailAPV(APIView):
    def get(self,request,id):
        try:
            platform = StreamPlatform.objects.get(pk=id)
        except StreamPlatform.DoesNotExist:
            return Response({"Error":"Not Found!"},status=status.HTTP_400_BAD_REQUEST)    
        serializer = StreamPlatform_Serializer(platform)
        return Response(serializer.data)
    
    def put(self,request,id):
        platform = StreamPlatform.objects.get(pk=id)
        serializer = StreamPlatform_Serializer(platform,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def delete(self,request,id):
        platform = StreamPlatform.objects.get(pk=id)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        