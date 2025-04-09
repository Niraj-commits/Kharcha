from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from .models import *

# Create your views here.

def home(request):
    
    cards = card.objects.all()
    context = {"cards":cards}
    
    return render(request,'home.html',context)

def add_card(request):
    
    if request.method == "POST":
        name = request.POST.get('name')
        
        card.objects.create(name = name)
        return redirect('/')
    
    return render(request,'add_card.html')
        