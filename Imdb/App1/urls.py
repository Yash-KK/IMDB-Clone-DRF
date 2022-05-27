from django.urls import path
from . import views

urlpatterns = [
   path("list/",views.WatchListAPV.as_view(),name='watch-list'),
   path("list/<int:id>",views.WatchDetailAPV.as_view(),name='watch-detail'),
   
   path("stream/",views.StreamListAPV.as_view(),name='stream-list'),
   path("stream/<int:id>",views.StreamDetailAPV.as_view(),name='stream-detail')
]
