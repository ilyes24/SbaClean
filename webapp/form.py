from Accounts.models import MyUser
from Address.models import *
from Post.models import *
from django import forms

from django.contrib.auth.forms import UserCreationForm

class UserRegistreForm(UserCreationForm):
    email=forms.EmailField()
    first_name=forms.CharField(required=True)
    last_name=forms.CharField(required=True)
    phone_number=forms.CharField(max_length=12,required=True)
    address=forms.CharField(required=True) 
    City=forms.ChoiceField(choices=[(City.id, City.name) for City in City.objects.all()])
   
    class Meta:
        model=MyUser
        fields=['username','email','first_name','last_name','phone_number','address','City','password1','password2']
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = MyUser
        fields = ['username','password']       
class UserComment(forms.ModelForm):
    # comment_owner= forms.ChoiceField(choices=[(MyUser.id, MyUser.username) for MyUser in MyUser.objects.all()])
    post=forms.ChoiceField(choices=[(Post.id, Post.title) for Post in Post.objects.all()])
    class Meta():
        model = Comment
        fields = ['post','description']    