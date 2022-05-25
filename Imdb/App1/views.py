from django.http import HttpResponse
from django.shortcuts import render

from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status

from .serializer import (
    Movie_Serializer
)
from .models import (
    Movie
)

# Create your views here.
class MovieListAPV(APIView):
    def get(self,request):
        movies = Movie.objects.all()
        serializer = Movie_Serializer(movies,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = Movie_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    
        
class MovieDetailAPV(APIView):
    def get(self,request,id):
        try:
            movie = Movie.objects.get(pk=id)
        except Movie.DoesNotExist:
            return Response({"error":"Not Found!"},status=status.HTTP_400_BAD_REQUEST)    
        serializer = Movie_Serializer(movie)
        return Response(serializer.data)
        
    def put(self,request,id):
        movie = Movie.objects.get(pk=id)
        serializer = Movie_Serializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)                
        
    def delete(self,request,id):
        movie = Movie.objects.get(pk=id)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    