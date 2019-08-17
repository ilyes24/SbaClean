from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.translation import gettext as _
from django.db import transaction
from .models import *
from .form import *
from Post.models import *
from Anomaly.models import *
from Address.models import *
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
    "url": "dashboard:dashboard_events",
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
    "url": "dashboard:dashboard_comments",
    "icon": "comment"
    },
    {
    "title": "Signalements",
    "status": "",
    "url": "dashboard:dashboard_reports",
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
    anomalies = Anomaly.objects.all()
    context = {"menu": menu, "anomalies": anomalies }
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

def dashboard_users_edit(request):
    menu_active('Utilisateurs')
    if request.method == 'POST' and request.POST.get('action') == 'delete':
        user_id = request.POST.get('user_id')
        users = MyUser.objects.filter(id=user_id).delete()
    users = MyUser.objects.all()
    context = {'menu': menu, 'users': users}
    return render(request, 'users.html', context)

def dashboard_events(request):
    menu_active('Evénements')
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'delete':
            post_id = request.POST.get('post_id')
            posts = Post.objects.filter(id=post_id).delete()
    events = Event.objects.all()
    context = {"menu": menu, "events": events }
    return render(request, 'events.html', context)

def dashboard_event_approve(request, eid):
    event = Event.objects.filter(id=eid)[0].approve()
    return redirect('dashboard:dashboard_events')

def dashboard_events_edit(request):
    menu_active('Evénements')
    context = {'menu': menu, }
    return render(request, 'events.html', context)

def dashboard_comments(request):
    menu_active('Commentaires') 
    if request.method == 'POST' and request.POST.get('action') == 'delete':
        comment_id = request.POST.get('comment_id')
        Comment.objects.filter(id=user_id).delete()
    comments = Comment.objects.all()
    context = {'menu': menu, 'comments': comments}
    return render(request, 'comments.html', context)

def dashboard_comments_edit(request):
    menu_active('Commentaires')    
    context = {'menu': menu, }
    return render(request, 'comments.html', context)

def dashboard_reports(request):
    menu_active('Signalements')
    if request.method == 'POST' and request.POST.get('action') == 'delete':
        user_id = request.POST.get('user_id')
        users = MyUser.objects.filter(id=user_id).delete()
    users = MyUser.objects.all()    
    context = {'menu': menu, 'reports': reports}
    return render(request, 'reports.html', context)

def dashboard_reports_edit(request):
    menu_active('Signalements')
    context = {'menu': menu, }
    return render(request, 'reports.html', context)
