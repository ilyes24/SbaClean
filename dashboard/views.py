from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.translation import gettext as _
from django.db import transaction
from .models import *
from .form import *
from Post.models import *
from Accounts.models import *
from Event.models import *
import json 

menu = [
    {
    "title": "Dashboard",
    "status": "active",
    "url": "dashboard:dashboard",
    "icon": "dashboard"
    },
    {
    "title": "Anomalies",
    "status": "",
    "url": "dashboard:dashboard_anomalies",
    "icon": "report_problem"
    },
    {
    "title": "Evénements",
    "status": "",
    "url": "dashboard:dashboard",
    "icon": "calendar_today"
    },
    {
    "title": "Utilisateurs",
    "status": "",
    "url": "dashboard:dashboard_users",
    "icon": "person"
    },
    {
    "title": "Commentaires",
    "status": "",
    "url": "dashboard:dashboard",
    "icon": "comment"
    },
    {
    "title": "Signalements",
    "status": "",
    "url": "dashboard:dashboard",
    "icon": "info"
    }
]

def menu_active(title):
    for item in menu:
        if item["title"] == title:
            item["status"] = "active"
        else:
            item["status"] = ""

def dashboard_index(request):
    menu_active('Dashboard')
    context = {"menu": menu}
    return render(request, 'index_dashboard.html', context)

def dashboard_anomalies(request):
    menu_active('Anomalies')
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'delete':
            post_id = request.POST.get('post_id')
            posts = Post.objects.filter(id=post_id).delete()
    posts = Post.objects.all()
    context = {"menu": menu, "posts": posts }
    return render(request, 'anomalies.html', context)

def dashboard_anomalie_edit(request, pid):
    menu_active('Anomalies')
    post = Post.objects.get(id=pid)
    form = PostForm(request.POST or None, instance = post)
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'edit' and form.is_valid():
            form.save()
            return redirect('dashboard:dashboard_anomalies')

    context = {'menu': menu, 'post': post, 'form': form}
    return render(request, 'anomalie_edit.html', context)

def dashboard_users(request):
    menu_active('Utilisateurs')
    if request.method == 'POST' and request.POST.get('action') == 'delete':
        user_id = request.POST.get('user_id')
        users = MyUser.objects.filter(id=user_id).delete()
    users = MyUser.objects.all()
    context = {'menu': menu, 'users': users}
    return render(request, 'users.html', context)

def dashboard_events(request):
    menu_active('Evénements')
    context = {}
    return render(request, 'index_dashboard.html', context)

def dashboard_comments(request):
    menu_active('Commentaires')    
    context = {}
    return render(request, 'index_dashboard.html', context)

def dashboard_reports(request):
    menu_active('Signalements')
    context = {}
    return render(request, 'index_dashboard.html', context)
