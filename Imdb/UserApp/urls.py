from django.urls import path
from rest_framework.authtoken import views
from .views import registeration_view, logout_view
urlpatterns = [
    path("login/",views.obtain_auth_token,name='login'),
    path("register/",registeration_view,name='register'),
    path("logout/",logout_view,name='logout')
]
