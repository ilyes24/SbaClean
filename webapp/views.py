from django.contrib.auth import authenticate
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.http import *
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.template import RequestContext
from django.urls import reverse
from django.utils.translation import gettext as _
from django.db import transaction
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.views import APIView
import cloudinary.uploader
from .models import *
from Post.models import *
from Event.models import *
from Anomaly.models import *
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
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

class UploadView(APIView):
    parser_classes = (
        MultiPartParser,
        JSONParser,
    )

@login_required
def feed(request):
        user = request.user
        username = request.user.username
        postCity=Post.objects.filter(city=user.city)
        posts=Anomaly.objects.filter(archived=False,post__in= postCity)
        user_pic_post=[]
        for post in postCity:
                user_pic_post.append({'post':post,'post_owner':post.post_owner,'user_pic':base64.urlsafe_b64encode(post.post_owner.username.encode())})
        comments=Comment.objects.all()
        user_pic_comment=[]
        for comment in comments:
                user_pic_comment.append({'comment':comment,'comment_owner':comment.comment_owner,'user_pic':base64.urlsafe_b64encode(comment.comment_owner.username.encode())})
        reactions= Reaction.objects.filter(reaction_owner=request.user)
        user_pic=base64.urlsafe_b64encode(username.encode())
        userId= request.user.id
        qs = MyUser.objects.all()
        query_limit = 5
        like_creat_nember=[]
        for reaction in reactions:
                like_creat_nember.append(reaction.post)

        if query_limit is not None:
                # get all users of the same city
                users = MyUser.objects.filter(city=user.city)
                user_pic_user=[]
                for user in users:
                        user_pic_user.append({'user':user,'user_pic':base64.urlsafe_b64encode(user.username.encode())})
                posts2=posts
                

                # Then doing the calculations
                users = users.annotate(rank_point=(Count('post__reactions', filter=Q(post__reactions__is_like=True)) - (
                        Count('post__reactions', filter=Q(post__reactions__is_like=False))))).filter(rank_point__gt=0)
                posts2 = posts2.annotate(rank_point=(Count('post__reactions', filter=Q(post__reactions__is_like=True)) )).filter(rank_point__gt=0)
                # And finaly, order the results
                users = users.order_by('-rank_point')[:query_limit]
                posts2=posts2.order_by('-rank_point')[:query_limit]
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
                        image= request.FILES['image'].read()
                        upload_data = cloudinary.uploader.upload(image)
                        image=upload_data['url']
                        title = request.POST.get('title')
                        city = request.POST.get('city')
                        longitude = request.POST.get('longitude')
                        latitude = request.POST.get('latitude')
                        description=request.POST.get('description')
                        post=Post.objects.create(title=title, post_owner=request.user,description=description,city=get_object_or_404(City,id=city),longitude=longitude,latitude=latitude,image=image)
                        post.save()
                        anomaly=Anomaly.objects.create(post=post,signaled=False)
                        anomaly.save()
        else:
                form=UserComment()
                form2=UserPost()            
        context = {'username':username,'user_pic':user_pic,'users':users,'posts':posts,'userId':userId,'comments':comments,'form':form,'form2':form2,'reactions':reactions,
        'like_creat_nember':like_creat_nember,'posts2':posts2,'user_pic_post':user_pic_post,'user_pic_comment':user_pic_comment,'user_pic_user':user_pic_user}         
        return render(request, 'feed.html', context)
def create_comment(request):
        if request.method == 'POST':
                post_id=int(request.POST['post_id'])
                post=get_object_or_404(Post,id=post_id)
                description=request.POST['description']
                Comment.objects.create(post=post, comment_owner=request.user,description=description)
                
        return HttpResponse('')

@login_required
def event(request):
        user = request.user
        username = request.user.username
        postCity=Post.objects.filter(city=user.city)
        events=Event.objects.filter(post__in= postCity)
        nb_participante=[]
        for event in events:
                nb_participante.append({'event':event,'nb_part':EventParticipation.objects.filter(event=event).count()})
        print(nb_participante)
        user_pic_post=[]
        for post in postCity:
                user_pic_post.append({'post':post,'post_owner':post.post_owner,'user_pic':base64.urlsafe_b64encode(post.post_owner.username.encode())})
        comments=Comment.objects.all()
        user_pic_comment=[]
        for comment in comments:
                user_pic_comment.append({'comment':comment,'comment_owner':comment.comment_owner,'user_pic':base64.urlsafe_b64encode(comment.comment_owner.username.encode())})
        user_pic_comment=[]
        for comment in comments:
                user_pic_comment.append({'comment':comment,'comment_owner':comment.comment_owner,'user_pic':base64.urlsafe_b64encode(comment.comment_owner.username.encode())})
        reactions= Reaction.objects.filter(reaction_owner=request.user)
        user_pic=base64.urlsafe_b64encode(username.encode())
        userId= request.user.id
        qs = MyUser.objects.all()
        query_limit = 5
        like_creat_nember=[]
        for reaction in reactions:
                like_creat_nember.append(reaction.post)

        if query_limit is not None:
                  # get all users of the same city
                users = MyUser.objects.filter(city=user.city)
                user_pic_user=[]
                for user in users:
                        user_pic_user.append({'user':user,'user_pic':base64.urlsafe_b64encode(user.username.encode())})
                posts2=events
                

                # Then doing the calculations
                users = users.annotate(rank_point=(Count('post__reactions', filter=Q(post__reactions__is_like=True)) - (
                        Count('post__reactions', filter=Q(post__reactions__is_like=False))))).filter(rank_point__gt=0)
                posts2 = posts2.annotate(rank_point=(Count('post__reactions', filter=Q(post__reactions__is_like=True)) )).filter(rank_point__gt=0)
                # And finaly, order the results
                users = users.order_by('-rank_point')[:query_limit]
                posts2=posts2.order_by('-rank_point')[:query_limit]
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
                        image= request.FILES['image'].read()
                        upload_data = cloudinary.uploader.upload(image)
                        image=upload_data['url']
                        title = request.POST.get('title')
                        city = request.POST.get('city')
                        longitude = request.POST.get('longitude')
                        latitude = request.POST.get('latitude')
                        description=request.POST.get('description')
                        max_participants =request.POST.get('max_participants')
                        starts_at = request.POST.get('starts_at')
                        post=Post.objects.create(title=title, post_owner=request.user,description=description,city=get_object_or_404(City,id=city),longitude=longitude,latitude=latitude,image=image)
                        post.save()
                        event=Event.objects.create(post=post, max_participants=max_participants, starts_at=starts_at)
                        event.save()
        else:
                form=UserComment()
                form2=UserPost()            
        context = {'username':username,'user_pic':user_pic,'events':events,'userId':userId,'users':users,'comments':comments,'form':form,'form2':form2,'reactions':reactions,'like_creat_nember':like_creat_nember,
        'posts2':posts2,'user_pic_post':user_pic_post,'user_pic_comment':user_pic_comment,'user_pic_user':user_pic_user,'nb_participante': nb_participante}         
        return render(request, 'event.html', context)
@login_required
def Myposts(request):
        user = request.user
        username = request.user.username
        posts=Anomaly.objects.filter(archived=False)
        Myposts=Post.objects.filter(post_owner=user)
        comments=Comment.objects.all()
        user_pic_comment=[]
        for comment in comments:
                user_pic_comment.append({'comment':comment,'comment_owner':comment.comment_owner,'user_pic':base64.urlsafe_b64encode(comment.comment_owner.username.encode())})
        reactions= Reaction.objects.filter(reaction_owner=request.user)
        user_pic=base64.urlsafe_b64encode(username.encode())
        userId= request.user.id
        qs = MyUser.objects.all()
        query_limit = 5
        like_creat_nember=[]
        for reaction in reactions:
                like_creat_nember.append(reaction.post)

        if query_limit is not None:
                  # get all users of the same city
                users = MyUser.objects.filter(city=user.city)
                user_pic_user=[]
                for user in users:
                        user_pic_user.append({'user':user,'user_pic':base64.urlsafe_b64encode(user.username.encode())})
                posts2=posts
                

                # Then doing the calculations
                users = users.annotate(rank_point=(Count('post__reactions', filter=Q(post__reactions__is_like=True)) - (
                        Count('post__reactions', filter=Q(post__reactions__is_like=False))))).filter(rank_point__gt=0)
                posts2 = posts2.annotate(rank_point=(Count('post__reactions', filter=Q(post__reactions__is_like=True)) )).filter(rank_point__gt=0)
                # And finaly, order the results
                users = users.order_by('-rank_point')[:query_limit]
                posts2=posts2.order_by('-rank_point')[:query_limit]
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
        context = {'username':username,'user_pic':user_pic,'posts':posts,'userId':userId,'users':users,'comments':comments,'form':form,'form2':form2,'reactions':reactions,'like_creat_nember':like_creat_nember,
        'posts2':posts2, 'Myposts':Myposts,'user_pic_user':user_pic_user,'user_pic_comment':user_pic_comment}         
        return render(request, 'Myposts.html', context)
@login_required
def Myreactions(request):
        user = request.user
        username = request.user.username
        posts=Anomaly.objects.filter(archived=False)
        postCity=Post.objects.filter()
        user_pic_post=[]
        for post in postCity:
                user_pic_post.append({'post':post,'post_owner':post.post_owner,'user_pic':base64.urlsafe_b64encode(post.post_owner.username.encode())})
        Myreactions=Reaction.objects.filter(reaction_owner=user)
        Mycomments=Comment.objects.filter(comment_owner=user)
        Mycomments2=[]
        for Vtcomment in Mycomments:
                if Vtcomment.post not in Mycomments2:
                        Mycomments2.append(Vtcomment.post)
        valide_comments=[]
        for Vcomment in Myreactions:
                valide_comments.append(Vcomment.post)
        comments=Comment.objects.all()
        user_pic_comment=[]
        for comment in comments:
                user_pic_comment.append({'comment':comment,'comment_owner':comment.comment_owner,'user_pic':base64.urlsafe_b64encode(comment.comment_owner.username.encode())})
        reactions= Reaction.objects.filter(reaction_owner=request.user)
        user_pic=base64.urlsafe_b64encode(username.encode())
        userId= request.user.id
        qs = MyUser.objects.all()
        query_limit = 5
        like_creat_nember=[]
        for reaction in reactions:
                like_creat_nember.append(reaction.post)

        if query_limit is not None:
                  # get all users of the same city
                users = MyUser.objects.filter(city=user.city)
                user_pic_user=[]
                for user in users:
                        user_pic_user.append({'user':user,'user_pic':base64.urlsafe_b64encode(user.username.encode())})
                posts2=posts
                

                # Then doing the calculations
                users = users.annotate(rank_point=(Count('post__reactions', filter=Q(post__reactions__is_like=True)) - (
                        Count('post__reactions', filter=Q(post__reactions__is_like=False))))).filter(rank_point__gt=0)
                posts2 = posts2.annotate(rank_point=(Count('post__reactions', filter=Q(post__reactions__is_like=True)) )).filter(rank_point__gt=0)
                # And finaly, order the results
                users = users.order_by('-rank_point')[:query_limit]
                posts2=posts2.order_by('-rank_point')[:query_limit]
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
        context = {'username':username,'user_pic':user_pic,'posts':posts,'userId':userId,'users':users,'comments':comments,'form':form,'form2':form2,'reactions':reactions,'like_creat_nember':like_creat_nember,
        'posts2':posts2, 'Myreactions':Myreactions,'Mycomments':Mycomments2, 'valide_comments':valide_comments,'user_pic_user':user_pic_user,'user_pic_comment':user_pic_comment,'user_pic_post':user_pic_post}         
        return render(request, 'Myreactions.html', context)

def like_post(request):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    reaction = Reaction.objects.filter(reaction_owner=request.user, post=post)
    reaction_nb = len(reaction)
    if reaction_nb == 0:
        reaction2 = Reaction.objects.create(reaction_owner=request.user, post=post, is_like=True)
        reaction2.save()

    else:
        if reaction.values('is_like')[0].get('is_like') == True:
            reaction.delete()
        else:
            reaction.delete()
            reaction2 = Reaction.objects.create(reaction_owner=request.user, post=post, is_like=True)
            reaction2.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def comment_delete(request):
    comment = get_object_or_404(Comment, id=int(request.POST['comment_id']))
    comment.delete()

    return HttpResponse('')


def dislike_post(request):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    reaction = Reaction.objects.filter(reaction_owner=request.user, post=post)
    reaction_nb = len(reaction)
    if reaction_nb == 0:
        reaction2 = Reaction.objects.create(reaction_owner=request.user, post=post, is_like=False)
        reaction2.save()

    else:
        if reaction.values('is_like')[0].get('is_like') == True:
            reaction.delete()
            reaction2 = Reaction.objects.create(reaction_owner=request.user, post=post, is_like=False)
            reaction2.save()
        else:
            reaction.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def signaled(request):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    anomaly = get_object_or_404(Anomaly, post=post)
    anomaly.signaled = True
    anomaly.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
def Participate(request):
        if request.method == 'POST':
                
                event_id=int(request.POST['event_id'])
                event=get_object_or_404(Event,id=event_id)
                nb_participante=EventParticipation.objects.filter(event=event).count()
                if nb_participante < event.max_participants:
                        if EventParticipation.objects.filter(event=event, user=request.user) :
                                return HttpResponse('')
                        else: 
                                EventParticipation.objects.create(event=event, user=request.user)
                else:
                        HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
                
        return HttpResponse('')


@login_required
def logout(request):
    auth_logout(request)
    print(request, "Logged out successfully!")
    return redirect('/')


def login(request):
    if request.user.is_authenticated :
        return redirect('/')  
    else:        
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
        if request.user.is_authenticated :
                return redirect('/')
        else:
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
        args = {'username': username, 'form': form, 'form2': form2}
        return render(request, 'profile.html', args)

    elif 'passwordCH' in request.POST:
        form2 = PasswordChangeForm(user=request.user, data=request.POST)
        if form2.is_valid():
            form2.save()
            update_session_auth_hash(request, form2.user)
            messages.add_message(request, messages.SUCCESS, 'Sucessfully changed password.')
        else:
            messages.add_message(request, messages.ERROR, 'Password change unsuccessful.')

        form = EditProfileForm(instance=request.user)
        args = {'username': username, 'form': form, 'form2': form2}
        return render(request, 'profile.html', args)
    else:
        messages.add_message(request, messages.SUCCESS, 'Remplire le formulair.')
        form = EditProfileForm(instance=request.user)
        form2 = PasswordChangeForm(user=request.user)
        args = {'username': username, 'form': form, 'form2': form2}
        return render(request, 'profile.html', args)


def error404(request, exception):
    context = {}
    return render(request, 'index.html', context)


def handler404(request, exception, template_name="index.html"):
    response = render_to_response("index.html")
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render_to_response('index.html', {}, context_instance=RequestContext(request))
    response.status_code = 500
    return response
