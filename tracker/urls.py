from django.urls import path
from .views import *

urlpatterns = [
    path("",home),
    path('add_card/',add_card,name='add_card'),
    path('add_card/<pk>',view_card_details,name="view_details")
]