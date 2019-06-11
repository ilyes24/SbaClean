
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.translation import gettext as _
from django.db import transaction
from .models import *

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
    context = {}
    return render(request, 'login.html', context)

def register(request):
    context = {}
    return render(request, 'register.html', context)

def post_details(request):
    context = {}
    return render(request, 'post_details.html', context)