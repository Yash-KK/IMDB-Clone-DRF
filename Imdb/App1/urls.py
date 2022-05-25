from django.urls import path
from . import views

urlpatterns = [
   path("list/",views.MovieListAPV.as_view(),name='movie-list'),
   path("list/<int:id>",views.MovieDetailAPV.as_view(),name='movie-detail')
]
