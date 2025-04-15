from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from .models import *
from .filter import *

# Create your views here.

def home(request):
    
    cards = card.objects.all()
    item_filter = CardFilter(request.GET,queryset=cards)
    cards = item_filter.qs
    context = {"cards":cards,"filter":item_filter}
    
    return render(request,'home.html',context)

def add_card(request):
    
    if request.method == "POST":
        name = request.POST.get('name')
        
        card.objects.create(name = name)
        return redirect('/')
    
    return render(request,'add_card.html')


def view_card_details(request,pk):
    
    card_details = card.objects.get(pk = pk)
    detail = info.objects.filter(card = card_details)
    item_filter = InfoFilter(request.GET,queryset=detail)
    detail = item_filter.qs
    
    

    
    total_amount = 0
    for item in detail:
        
        if item.entry_type == "income":
            total_amount += item.amount
        
        elif item.entry_type == "expense":
            total_amount -= item.amount
    context = {"expense_entries":detail,"card_details":card_details,"filter":item_filter,"total_amount":total_amount}
    
    


    return render(request,"card_details/view.html",context)

def Add_Expense(request,pk):
    card_details = card.objects.get(pk = pk)
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        amount = request.POST.get('amount')
        entry_type = "expense"
        linked_card = card_details
        
        info.objects.create(title = title,description = description,amount=amount,entry_type=entry_type,card = linked_card)
        return redirect('view_details',pk=pk)
    
    context= {"card_details": card_details}
    return render(request,'card_details/add_expense.html',context)


def Add_Income(request,pk):
    card_details = card.objects.get(pk = pk)
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        amount = request.POST.get('amount')
        entry_type = "income"
        linked_card = card_details
        
        info.objects.create(title = title,description = description,amount=amount,entry_type=entry_type,card = linked_card)
        return redirect('view_details',pk=pk)
    
    context= {"card_details": card_details}
    return render(request,'card_details/add_income.html',context)