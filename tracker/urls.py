from django.urls import path
from .views import *

urlpatterns = [
    path("",home,name="home"),
    path('add_card/',add_card,name='add_card'),
    path('add_card/<pk>',view_card_details,name="view_details"),
    path('add_card/<pk>/add_income',Add_Income,name="add_income"),
    path('add_card/<pk>/add_expense',Add_Expense,name="add_expense"),
]