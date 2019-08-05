from django.shortcuts import render
from django.http import JsonResponse
from Anomaly.models import Anomaly
from django.views.decorators.csrf import csrf_exempt, csrf_protect
# Create your views here.
def index(request):
    pass

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

