from django.urls import path
from . import views

urlpatterns = [
   path("list/",views.WatchListAPV.as_view(),name='watch-list'),
   path("<int:pk>/",views.WatchDetailAPV.as_view(),name='watch-detail'),
   
   path("stream/",views.StreamListAPV.as_view(),name='stream-list'),
   path("stream/<int:pk>",views.StreamDetailAPV.as_view(),name='stream-detail'),
   
   path("stream/<int:pk>/review-create/",views.ReviewCreate.as_view(),name='review-list'),
   path("stream/<int:pk>/review/",views.ReviewList.as_view(),name='review-list'),
   path("stream/review/<int:pk>/",views.ReviewDetail.as_view(),name='review-detail')   
]
