from django.http import HttpResponse
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import ValidationError

from .serializer import (
    Review_Serializer,
    WatchList_Serializer,
    StreamPlatform_Serializer
    
)
from .models import (
    Review,
    WatchList,
    StreamPlatform
)

# Create your views here.

"""
Reviews Related
"""
class ReviewList(generics.ListAPIView):
    # queryset = Review.objects.all()
    serializer_class = Review_Serializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)
    
class ReviewCreate(generics.CreateAPIView):
    serializer_class = Review_Serializer
    
    def get_queryset(self):
        return Review.objects.all()
    
    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        movie = WatchList.objects.get(pk=pk)
        
        review_user = self.request.user
        rev = Review.objects.filter(watchlist=movie,review_user=review_user)
        if rev.exists():
            raise ValidationError("User already Reviewed this Movie!")
        
        serializer.save(watchlist=movie,review_user=review_user)
        

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = Review_Serializer    

     
"""
WatchList Related
"""
class WatchListAPV(generics.ListCreateAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchList_Serializer

class WatchDetailAPV(generics.RetrieveUpdateDestroyAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchList_Serializer    
    

"""Stream Platform related"""    
class StreamListAPV(generics.ListCreateAPIView):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatform_Serializer

class StreamDetailAPV(generics.RetrieveUpdateDestroyAPIView):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatform_Serializer    