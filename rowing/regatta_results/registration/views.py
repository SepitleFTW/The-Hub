from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .forms import UserRegistrationForm
import requests
from django.http import JsonResponse
from django.contrib.auth import views as auth_views
from django.contrib import messages

def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data["password"])
            new_user.save()
            # Auto log in the user after registration
            user = authenticate(username=new_user.username, password=form.cleaned_data["password"])
            if user is not None:
                auth_login(request, user)
                return redirect("home")  # This takes them to the welcome screen
            else:
                messages.error(request, "Registration successful, but auto login failed. Please log in manually.")
                return redirect("login")
    else:
        form = UserRegistrationForm()
    return render(request, "registration.html", {"form": form})

def homepage(request):
    return render(request, "home.html")

def weather(request):
    return render(request, "weather.html")

def regattas(request):
    return render(request, "regattas.html")

def custom_login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("home")  # Redirect to the home page after successful login
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'login.html')
