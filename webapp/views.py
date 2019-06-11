from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.translation import gettext as _
from django.db import transaction
from .models import *

def index(request):
    context = {}
    return render(request, 'main/index.html', context)

def account(request):
    context = {}
    return render(request, 'main/account.html', context)

def feed(request):
    context = {}
    return render(request, 'main/feed.html', context)

def login(request):
    context = {}
    return render(request, 'main/login.html', context)

def post_details(request):
    context = {}
    return render(request, 'main/post_details.html', context)