from django.urls import path
from .views import *
from django.views.generic import TemplateView

urlpatterns = [
    path("",home,name="home"),
    path('add_card/',add_card,name='add_card'),
    path('add_card/<pk>',view_card_details,name="view_details"),
    path('add_card/<pk>/edit',edit_card,name="edit_details"),
    path('add_card/<pk>/delete',delete_card,name="delete_details"),
    path('add_card/<pk>/add_income',Add_Income,name="add_income"),
    path('add_card/<pk>/add_expense',Add_Expense,name="add_expense"),
    path('add_card/<pk>/<int:edit_id>',edit_card_details,name="edit_details"),
    path('add_card/<pk>/<int:delete_id>/delete',delete_card_details,name="delete_details"),
    path('sw.js', service_worker, name='service_worker'),
    path('sw.js', TemplateView.as_view(template_name='sw.js', content_type='application/javascript'), name='sw.js'),
]