from django.http import HttpResponse
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .serializer import (
    Movie_Serializer
)
from .models import (
    Movie
)
# Create your views here.

@api_view(['GET','POST'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = Movie_Serializer(movies,many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = Movie_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
   

@api_view(['GET','PUT','DELETE'])
def movie_detail(request,id):
    if request.method == 'GET':
        try:
            movie = Movie.objects.get(pk=id)
        except Movie.DoesNotExist:
            return Response({"error":"Error Found!"},status=status.HTTP_404_NOT_FOUND)     
                   
        serializer = Movie_Serializer(movie)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        movie = Movie.objects.get(pk=id)
        serializer = Movie_Serializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)        
    
    if request.method == 'DELETE':
        movie = Movie.objects.get(pk=id)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
