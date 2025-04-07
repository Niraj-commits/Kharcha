from django.shortcuts import render
from django.contrib import messages
from .models import *

# Create your views here.

def home(request):
    
    datas = info.objects.all()
    context = {"data":datas}
    
    return render(request,'home.html',context)