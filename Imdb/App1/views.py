from django.http import HttpResponse
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated

from .permission import isAdminOrReadOnly, isOwnerOrReadOnly
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
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Review.objects.all()
    
    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        moviee = WatchList.objects.get(pk=pk)
        
        review_user = self.request.user
        rev = Review.objects.filter(watchlist=moviee,review_user=review_user)
        if rev.exists():
            raise ValidationError("User already Reviewed this Movie!")
        
        if moviee.num_rating == 0:
            moviee.avg_rating = serializer.validated_data['rating']
        else:
            moviee.avg_rating = (moviee.avg_rating + serializer.validated_data['rating'])/2
        moviee.num_rating +=1        
        moviee.save()        
        serializer.save(watchlist=moviee,review_user=review_user)
        

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [isOwnerOrReadOnly]
    queryset = Review.objects.all()
    serializer_class = Review_Serializer    

     
"""
WatchList Related
"""
class WatchListAPV(generics.ListCreateAPIView): 
    permission_classes = [isAdminOrReadOnly]
    queryset = WatchList.objects.all()
    serializer_class = WatchList_Serializer

class WatchDetailAPV(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [isAdminOrReadOnly]
    queryset = WatchList.objects.all()
    serializer_class = WatchList_Serializer    
    

"""Stream Platform related"""    
class StreamListAPV(generics.ListCreateAPIView):
    permission_classes = [isAdminOrReadOnly]
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatform_Serializer

class StreamDetailAPV(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [isAdminOrReadOnly]
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatform_Serializer    