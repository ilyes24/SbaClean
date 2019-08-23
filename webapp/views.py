from django.contrib.auth import authenticate
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils.translation import gettext as _
from django.db import transaction
from .models import *
from Post.models import *
from Event.models import *
from Anomaly.models import *
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from .form import *
import base64
from social_django.utils import psa, load_strategy
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models.aggregates import Count
from django.db.models import Q
from django.db.models.query import QuerySet
UserModel = get_user_model()

def index(request):
    context = {}
    return render(request, 'index.html', context)

@login_required
def account(request):
    context = {}
    return render(request, 'account.html', context)

@login_required
def feed(request):
        user = request.user
        username = request.user.username
        posts=Anomaly.objects.all()
        comments=Comment.objects.all()
        reactions= Reaction.objects.filter(reaction_owner=request.user)
        user_pic=base64.urlsafe_b64encode(username.encode())
        userId= request.user.id
        qs = MyUser.objects.all()
        query_limit = 5
        like_creat_nember=len(reactions)

        if query_limit is not None:
                # get all users of the same city
                users = MyUser.objects.filter(city=user.city)

                # Then doing the calculations
                users = users.annotate(rank_point=(Count('post__reactions', filter=Q(post__reactions__is_like=True)) - (
                        Count('post__reactions', filter=Q(post__reactions__is_like=False))))).filter(rank_point__gt=0)
                # And finaly, order the results
                users = users.order_by('-rank_point')[:query_limit]
        if request.method == 'POST':
                form=UserComment(request.POST or None)
                form2=UserPost(request.POST or None)
                if form.is_valid():
                        if request.POST.get('post_id'):
                                post_id=int(request.POST.get('post_id'))
                                post=get_object_or_404(Post,id=post_id)
                                description=request.POST.get('description')
                                comment=Comment.objects.create(post=post, comment_owner=request.user,description=description)
                                comment.save()
                if form2.is_valid():
                        title = request.POST.get('title')
                        city = request.POST.get('city')
                        longitude = request.POST.get('longitude')
                        latitude = request.POST.get('latitude')
                        description=request.POST.get('description')
                        post=Post.objects.create(title=title, post_owner=request.user,description=description,city=get_object_or_404(City,id=city),longitude=longitude,latitude=latitude)
                        post.save()
                        anomaly=Anomaly.objects.create(post=post,signaled=False)
                        anomaly.save()
        else:
                form=UserComment()
                form2=UserPost()            
        context = {'username':username,'user_pic':user_pic,'users':users,'posts':posts,'userId':userId,'comments':comments,'form':form,'form2':form2,'reactions':reactions,
        'like_creat_nember':like_creat_nember}         
        return render(request, 'feed.html', context)
@login_required
def event(request):
        user = request.user
        username = request.user.username
        events=Event.objects.all()
        comments=Comment.objects.all()
        user_pic=base64.urlsafe_b64encode(username.encode())
        userId= request.user.id
        qs = MyUser.objects.all()
        query_limit = 5

        if query_limit is not None:
                # get all users of the same city
                users = MyUser.objects.filter(city=user.city)

                # Then doing the calculations
                users = users.annotate(rank_point=(Count('post__reactions', filter=Q(post__reactions__is_like=True)) - (
                        Count('post__reactions', filter=Q(post__reactions__is_like=False))))).filter(rank_point__gt=0)
                # And finaly, order the results
                users = users.order_by('-rank_point')[:query_limit]
        if request.method == 'POST':
                form=UserComment(request.POST or None)
                form2=UserPost(request.POST or None)
                if form.is_valid():
                        if request.POST.get('post_id'):
                                post_id=int(request.POST.get('post_id'))
                                post=get_object_or_404(Post,id=post_id)
                                description=request.POST.get('description')
                                comment=Comment.objects.create(post=post, comment_owner=request.user,description=description)
                                comment.save()
                if form2.is_valid():
                        title = request.POST.get('title')
                        city = request.POST.get('city')
                        longitude = request.POST.get('longitude')
                        latitude = request.POST.get('latitude')
                        description=request.POST.get('description')
                        max_participants =request.POST.get('max_participants')
                        starts_at = request.POST.get('starts_at')
                        post=Post.objects.create(title=title, post_owner=request.user,description=description,city=get_object_or_404(City,id=city),longitude=longitude,latitude=latitude)
                        post.save()
                        event=Event.objects.create(post=post, max_participants=max_participants, starts_at=starts_at)
                        event.save()
        else:
                form=UserComment()
                form2=UserPost()            
        context = {'username':username,'user_pic':user_pic,'events':events,'userId':userId,'users':users,'comments':comments,'form':form,'form2':form2}         
        return render(request, 'event.html', context)
def like_post(request):
        post=get_object_or_404(Post,id=request.POST.get('post_id'))
        reaction= Reaction.objects.filter(reaction_owner=request.user,post=post)
        reaction_nb=len(reaction)
        if reaction_nb==0 :
                reaction2=Reaction.objects.create(reaction_owner=request.user,post=post,is_like=True)
                reaction2.save()
                
        else:
                if reaction.values('is_like')[0].get('is_like')==True:
                        reaction.delete()
                else:
                        reaction.delete()
                        reaction2=Reaction.objects.create(reaction_owner=request.user,post=post,is_like=True)
                        reaction2.save()
                
        return redirect('feed')
def dislike_post(request):
        post=get_object_or_404(Post,id=request.POST.get('post_id'))
        reaction= Reaction.objects.filter(reaction_owner=request.user,post=post)
        reaction_nb=len(reaction)
        if reaction_nb==0 :
                reaction2=Reaction.objects.create(reaction_owner=request.user,post=post,is_like=False)
                reaction2.save()
                
        else:
                if reaction.values('is_like')[0].get('is_like')==True:
                        reaction.delete()
                        reaction2=Reaction.objects.create(reaction_owner=request.user,post=post,is_like=False)
                        reaction2.save()
                else:
                        reaction.delete()
                
        return redirect('feed')
@login_required
def logout(request):
    auth_logout(request)
    print(request, "Logged out successfully!")
    return redirect('/')

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
                        return HttpResponse("Your account is inactive.")
        else:
            errors = '<div class="alert alert-danger" role="alert">Nom d\'utilisateur ou mot de passe incorrect</div>'
            context = {'form':form, 'errors': errors}
            return render(request, 'login.html', context)
    else:
            return render(request, 'login.html', context)
    
def register(request):
        if (request.method == 'POST'):
                form=UserRegistreForm(request.POST)
                if form.is_valid():
                        user = form.save(commit=False)
                        user.city_id = form.cleaned_data.get('City')
                        user.save()
                        raw_password = request.POST.get('password1')
                        raw_user=request.POST.get('username')
                        user = authenticate(username=raw_user, password=raw_password)
                        auth_login(request, user)
                        return redirect('feed')
                else:
                        context = {'form':form}
                        return render(request, 'register.html', context)
        else:
                partial_token = None
                if request.GET.get('partial_token'):
                        strategy = load_strategy()
                        partial_token = request.GET.get('partial_token')
                        partial = strategy.partial_load(partial_token)
                        data = partial.data['kwargs']['details']
                        form=UserRegistreForm(initial = {'username': data['username'],'email' :data['email'], 'First_name': data['first_name'],'Last_name': data['last_name']})
                        context = {'form':form}
                        return render(request, 'register.html', context)
                else:
                        form=UserRegistreForm()
                        context = {'form':form}
                        return render(request, 'register.html', context)
        
def social_auth(request):
        strategy = load_strategy()
        partial_token = request.GET.get('partial_token')
        partial = strategy.partial_load(partial_token)

        email = partial.data['kwargs']['details']['email']
        user = UserModel.objects.get(email=email)
        auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('feed')

@login_required
def post_details(request):
    context = {}
    return render(request, 'post_details.html', context)
@login_required
def profile(request):
    username = request.user.username
    if 'details' in request.POST:
      form = EditProfileForm(request.POST, instance=request.user)
      if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, 'Sucessfully changed informations.')
      else:
        messages.add_message(request, messages.ERROR, 'Could not edit account details.')

      form2 = PasswordChangeForm(user=request.user)
      args = {'username':username,'form': form, 'form2': form2 }
      return render(request, 'profile.html', args)

    else:
      form2 = PasswordChangeForm(user=request.user, data=request.POST)
      if form2.is_valid():
        form2.save()
        update_session_auth_hash(request, form2.user)
        messages.add_message(request, messages.SUCCESS, 'Sucessfully changed password.')
      else:
        messages.add_message(request, messages.ERROR, 'Password change unsuccessful.')

      form = EditProfileForm(instance=request.user)
      args = {'username':username,'form': form, 'form2': form2 }
      return render(request, 'profile.html', args) 


def error404(request, exception):
    context = {}
    return render(request, 'index.html', context)
