from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/',CustomLogin,name="login"),
    path('register/',Register,name="register"),
    path('logout/', logout,name="logout"),
]