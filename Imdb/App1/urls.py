from django.urls import path
from . import views

urlpatterns = [
    path("list/",views.movie_list,name='movie-list'),
    path("list/<int:id>",views.movie_detail,name='movie-detail')
]
