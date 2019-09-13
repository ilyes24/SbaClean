from django.shortcuts import render
from django.http import JsonResponse
from Anomaly.models import Anomaly
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import onesignal as onesignal_sdk
from .models import *
from geopy.distance import geodesic
from decimal import Decimal
import datetime# Create your views here.
def index(request):
    pass
onesignal_client = onesignal_sdk.Client(user_auth_key="YjI4NzQ0OGMtZWE3Zi00NTM1LTg5OWYtMmZmMjYxMDNlZjZi",
                                    app_auth_key="ZTc0YzcxNTktYTBkZS00M2VlLWI2MGMtMDM0YjZhMjM4NzMx",
                                    app_id="9bd315f4-1520-4d10-9994-d2285cd96d03")

@csrf_exempt
def update_posts_notification(request):

    if request.method == 'POST':
        count_old = request.POST['count']
        count_new = Anomaly.objects.count()

        if (count_new > int(count_old)):
            context = { "changed" : True }
            return JsonResponse(context)

        else:
            context = { "changed" : False }

            return JsonResponse(context)

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
        if (geodesic((user_latitude, user_longitude),(anomaly.post.latitude,anomaly.post.longitude)).kilometers > Decimal(distance)):
            context.append(anomaly)
    print(context)
    origin = (user_latitude, user_longitude)
    new_notification = onesignal_sdk.Notification(post_body={
    "data": {"id": context[0].pk},
    "headings": {"fr" : "Attention, "+context[0].post.title+" !","en" : "Attention, "+context[0].post.title+" !",},
    "contents": {"en": context[0].post.title + " a " + distance, "tr": "Mesaj"},
    "included_segments": ["Active Users"],
    
})
    onesignal_response = onesignal_client.send_notification(new_notification)
    print(onesignal_response.status_code)
    print(onesignal_response.json())
    return JsonResponse({"response": context[0].pk})

# send notification, it will return a response
