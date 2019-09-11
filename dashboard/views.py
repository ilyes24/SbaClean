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
from django.contrib.admin.views.decorators import staff_member_required
from datetime import datetime
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
    "title": "Anomalies archivées",
    "status": "",
    "url": "dashboard:dashboard_archives",
    "icon": "check_circle_outline"
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
    # {
    # "title": "Commentaires",
    # "status": "",
    # "url": "dashboard:dashboard_comments",
    # "icon": "comment"
    # },
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

@staff_member_required
def dashboard_index(request):
    menu_active('Dashboard')
    users_count = MyUser.objects.all().count()
    anomalies_count = Anomaly.objects.filter(archived=False).count()
    events_count = Event.objects.all().count()
    archives_count = Anomaly.objects.filter(archived=True).count()
    anomalies = Anomaly.objects.all()
    monthly = []
    now_month = datetime.now().month
    now_year = datetime.now().year
    for i in range(1,32):
        monthly.append(0)
    for a in anomalies:
        for i in range(1,32):
            if (a.post.created_at.day == i) and (a.post.created_at.month == now_month) and (a.post.created_at.year == now_year):
                monthly[i-1]+=1;
    stats = {
        "users": users_count,
        "anomalies": anomalies_count,
        "events": events_count,
        "archives": archives_count,
        "monthly": monthly
    }
    context = {"menu": menu, "stats": stats, "anomalies": anomalies}
    return render(request, 'index_dashboard.html', context)

@staff_member_required
def dashboard_anomalies(request):
    menu_active('Anomalies')
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'delete':
            post_id = request.POST.get('post_id')
            posts = Post.objects.filter(id=post_id).delete()
    anomalies = Anomaly.objects.filter(archived=False)
    context = {"menu": menu, "anomalies": anomalies }
    return render(request, 'anomalies.html', context)

@staff_member_required
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

@staff_member_required
def dashboard_anomalie_archive(request, pid):
    menu_active('Anomalies')
    anomaly = Anomaly.objects.get(post=pid)
    anomaly.archive()
    return redirect('dashboard:dashboard_anomalies')

@staff_member_required
def dashboard_archives(request):
    menu_active('Anomalies archivées')
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'delete':
            post_id = request.POST.get('post_id')
            posts = Post.objects.filter(id=post_id).delete()
    anomalies = Anomaly.objects.filter(archived=True)
    context = {"menu": menu, "anomalies": anomalies }
    return render(request, 'archives.html', context)

@staff_member_required
def dashboard_users(request):
    menu_active('Utilisateurs')
    if request.method == 'POST' and request.POST.get('action') == 'ban':
        user_id = request.POST.get('user_id')
        users = MyUser.objects.filter(id=user_id)[0].ban()
    users = MyUser.objects.all()
    context = {'menu': menu, 'users': users}
    return render(request, 'users.html', context)

@staff_member_required
def dashboard_users_edit(request):
    menu_active('Utilisateurs')
    context = {'menu': menu}
    return render(request, 'users.html', context)

@staff_member_required
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

@staff_member_required
def dashboard_event_approve(request, eid):
    event = Event.objects.filter(id=eid)[0].approve()
    return redirect('dashboard:dashboard_events')

@staff_member_required
def dashboard_events_edit(request):
    menu_active('Evénements')
    context = {'menu': menu, }
    return render(request, 'events.html', context)

@staff_member_required
def dashboard_comments(request):
    menu_active('Commentaires') 
    if request.method == 'POST' and request.POST.get('action') == 'delete':
        comment_id = request.POST.get('comment_id')
        Comment.objects.filter(id=user_id).delete()
    comments = Comment.objects.all()
    context = {'menu': menu, 'comments': comments}
    return render(request, 'comments.html', context)

@staff_member_required
def dashboard_comments_edit(request):
    menu_active('Commentaires')    
    context = {'menu': menu, }
    return render(request, 'comments.html', context)

@staff_member_required
def dashboard_reports(request):
    menu_active('Signalements')
    if request.method == 'POST' and request.POST.get('action') == 'ban':
        user_id = request.POST.get('user_id')
        users = MyUser.objects.filter(id=user_id)[0].ban()
    if request.method == 'POST' and request.POST.get('action') == 'delete':        
        post_id = request.POST.get('post_id')
        anomaly_id = request.POST.get('anomaly_id')
        post = Post.objects.filter(id=post_id).delete()
        anomaly = Anomaly.objects.filter(id=anomaly_id).delete()
    reports = AnomalySignal.objects.all()    
    context = {'menu': menu, 'reports': reports}
    return render(request, 'reports.html', context)

@staff_member_required
def dashboard_reports_edit(request):
    menu_active('Signalements')
    context = {'menu': menu, }
    return render(request, 'reports.html', context)
