from django.shortcuts import render, redirect
from .models import *
from django.contrib import auth
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login as auth_login  # Renamed login to avoid shadowing
from django.contrib import messages


# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect("/")

def CustomLogin(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)
            messages.success(request, "Welcome User")
            return redirect('/')
        else:
            messages.error(request, "Invalid Username or Password")

    return render(request, 'authentication/login.html')

from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.shortcuts import redirect, render

def Register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get('email')
        address = request.POST.get('address')
        password = request.POST.get('password')

        if len(password) > 8:
            hashed_password = make_password(password)
            User.objects.create(username=username, email=email, address=address, password=hashed_password)
            messages.success(request, "Registration successful")
            return redirect("login")
        else:
            messages.error(request, "Password length cannot be less than 8")
            return redirect('register')
    return render(request, "authentication/register.html")
