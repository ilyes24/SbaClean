from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.translation import gettext as _
from django.db import transaction
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .form import *

def index(request):
    context = {}
    return render(request, 'index.html', context)

def account(request):
    context = {}
    return render(request, 'account.html', context)

def feed(request):
    context = {}
    return render(request, 'feed.html', context)

def login(request):
    form=UserForm(request.POST)
    context = {'form':form}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
                if user.is_active:
                        auth_login(request,user)
                        return redirect('feed')
                else:
                        return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
             return render(request, 'login.html', context)
    
def register(request):
                form=UserRegistreForm(request.POST)
                context = {'form':form}
                if form.is_valid():
                        user = form.save(commit=False)
                        user.city_id = form.cleaned_data.get('City')
                        user.save()
                        raw_password = form.cleaned_data.get('password1')
                        raw_user=form.cleaned_data.get('username')
                        user = authenticate(username=raw_user, password=raw_password)
                        auth_login(request, user)
                        return redirect('feed')
                else:
                        form=UserRegistreForm()
                        return render(request, 'register.html', context)
        


def post_details(request):
    context = {}
    return render(request, 'post_details.html', context)

