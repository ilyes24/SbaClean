from .models import *
from django.shortcuts import render, redirect,get_object_or_404
from django.http import JsonResponse
from django.core import serializers

def post_comments(request,pk):
    comments = Comment.objects.filter(post = pk).values('id','comment_owner','description','post')
    results = {'results': list(comments)}

    return JsonResponse(results)

def post_picture(request,pk):
    picture = Picture.objects.filter(post = pk).values('id','photo_path','post')
    results = {'result': picture}

    return JsonResponse(results,safe=False)    

def user_reactions(request,pk):
    reactions = Reaction.objects.filter(reaction_owner = pk).values('id','reaction_owner','is_like','post')
    results =  list(reactions)

    return JsonResponse(results,safe=False)