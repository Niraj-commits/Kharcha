from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from .models import *
from .filter import *
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.http import HttpResponse
from django.conf import settings
import os

@login_required
def home(request):
    cards = card.objects.filter(created_by = request.user)
    item_filter = CardFilter(request.GET,queryset=cards)
    cards = item_filter.qs
    context = {"cards":cards,"filter":item_filter}

    return render(request,'home.html',context)

@login_required
def add_card(request):
    if request.method == "POST":
        name = request.POST.get('name')

        card.objects.create(name = name,created_by = request.user)
        messages.success(request,"Card Added Successfully")
        return redirect('/')

    return render(request,'add_card.html')

@login_required
def view_card_details(request,pk):

    card_details = card.objects.get(pk = pk)
    detail = info.objects.filter(card = card_details)
    item_filter = InfoFilter(request.GET,queryset=detail)
    detail = item_filter.qs
    entry_type_filter = request.GET.get('entry_type')

    total_amount = 0
    for item in detail:

        if item.entry_type == "income":
            total_amount += item.amount

        elif item.entry_type == "expense":
            total_amount -= item.amount
    context = {"expense_entries":detail,"card_details":card_details,"filter":item_filter,"total_amount":total_amount,'entry_type':entry_type_filter}
    return render(request,"card_details/view.html",context)

@login_required
def Add_Expense(request,pk):
    card_details = card.objects.get(pk = pk)
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        amount = request.POST.get('amount')
        entry_type = "expense"
        linked_card = card_details
        created_by = request.user

        info.objects.create(title = title,description = description,amount=amount,entry_type=entry_type,card = linked_card,created_by=created_by)
        messages.success(request,"Expense Added Successfully")
        return redirect('view_details',pk=pk)

    context= {"card_details": card_details}
    return render(request,'card_details/view.html',context)

@login_required
def Add_Income(request,pk):
    card_details = card.objects.get(pk = pk)
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        amount = request.POST.get('amount')
        entry_type = "income"
        linked_card = card_details
        created_by = request.user

        info.objects.create(title = title,description = description,amount=amount,entry_type=entry_type,card = linked_card,created_by = created_by)
        messages.success(request,"Income added successfully")
        return redirect('view_details',pk=pk)

    context= {"card_details": card_details}
    return render(request,'card_details/view.html',context)

@login_required
def edit_card_details(request,pk,edit_id):

    card_details = card.objects.get(pk = pk)
    item_detail = info.objects.get(id = edit_id)

    context = {"task":item_detail,"card_details":card_details}

    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        amount = request.POST.get('amount')
        selected_card = card_details

        item_detail.title = title
        item_detail.description = description
        item_detail.amount = amount
        item_detail.card = selected_card
        item_detail.save()
        return redirect('view_details',pk = pk)

    return render(request,'card_details/view.html',context)

@login_required
def delete_card_details(request,pk,delete_id):

    # card_details = card.objects.get(pk = pk)
    item_detail = info.objects.get(id = delete_id)

    item_detail.delete()
    return redirect('view_details',pk = pk)

@login_required
def edit_card(request,pk):

    card_detail = card.objects.get(pk = pk)
    context = {"card":card_detail}

    if request.method == "POST":
        name = request.POST.get('name')
        card_detail.name = name
        card_detail.save()

        messages.success(request,"Updated Successfully..")
        return redirect('/')

    return render(request,'home.html',context)

@login_required
def delete_card(request,pk):

    card_detail = card.objects.get(pk = pk)
    card_detail.delete()
    messages.success(request,"Deleted Successfully..")
    return redirect('/')

def service_worker(request):
    sw_path = os.path.join(settings.BASE_DIR, 'staticfiles', 'sw.js')
    with open(sw_path) as f:
        response = HttpResponse(f.read(), content_type='application/javascript')
    response['Service-Worker-Allowed'] = '/'
    return response