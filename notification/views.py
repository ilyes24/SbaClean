from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from Anomaly.models import Anomaly
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import onesignal as onesignal_sdk
from .models import *
from geopy.distance import geodesic
from decimal import Decimal
import datetime# Create your views here.
import os
from func_timeout import func_set_timeout

def index(request):
    pass
onesignal_client = onesignal_sdk.Client(user_auth_key=os.environ.get('onesignal_user_auth_key'),
                                    app_auth_key=os.environ.get('onesignal_app_auth_key'),
                                    app_id=os.environ.get('onesignal_app_id'),)


@csrf_exempt
def new_user(request):
    user_id = request.POST['user_id']
    user_opensignal_id = request.POST['user_opensignal_id']

    user = NotificationUser.objects.get(pk=user_id)
    if (user == None):
        user = NotificationUser.objects.create(user_opensignal_id= user_opensignal_id, 
            user= user_id, latitude="0", longitude="0")
        user.save()
    return HttpResponse('')

@csrf_exempt
def update_posts_notification(request):

    if request.method == 'POST':
        count_old = request.POST['count']
        city = request.POST['city']
        count_new = Anomaly.objects.filter(post__city = city).count()

        if (count_new > int(count_old)):
            context = { "changed" : True }
            return JsonResponse(context)

        else:
            context = { "changed" : False }

            return JsonResponse(context)

@func_set_timeout(45)
@csrf_exempt
def send_new_anomaly_notification(request):
    distance = request.POST.get('distance')
    user_latitude = request.POST.get('latitude')
    user_longitude = request.POST.get('longitude')
    post_id = request.POST.get('postId')
    time = request.POST.get('time')
    start_date = datetime.date(2005, 1, 1)
    anomaly_list = Anomaly.objects.filter(post__created_at__gte = start_date ).filter(post__pk__gt = post_id)
    context = []
    for anomaly in anomaly_list:
        if (geodesic((user_latitude, user_longitude),(anomaly.post.latitude,anomaly.post.longitude)).meters > Decimal(distance)):
            context.append(anomaly)
    if (len(context) > 0):
        anomaly = context[0]
        real_distance = geodesic((user_latitude, user_longitude),(anomaly.post.latitude,anomaly.post.longitude)).meters
        new_notification = onesignal_sdk.Notification(post_body={
        "data": {"id": context[0].pk, "postId" : post_id},
        "headings": {"fr" : "Attention, "+context[0].post.title+" !","en" : "Attention, "+context[0].post.title+" !",},
        "contents": {"en": context[0].post.title + " a " + str(real_distance) + " métres !",
             "fr": context[0].post.title + " a " + str(real_distance) + " métres !",},
        "included_segments": ["Active Users"],
    
    })
        timeout = datetime.datetime.now()
        onesignal_response = onesignal_client.send_notification(new_notification)
        print(onesignal_response.status_code)
        print(onesignal_response.json())
        return HttpResponse('')
    return HttpResponse('')

# send notification, it will return a response
