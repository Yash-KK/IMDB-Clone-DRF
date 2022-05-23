from django.http import HttpResponse
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializer import (
    Movie_Serializer
)
from .models import (
    Movie
)
# Create your views here.

@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = Movie_Serializer(movies,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request,id):
    movie = Movie.objects.get(pk=id)
    serializer = Movie_Serializer(movie)
    return Response(serializer.data)
