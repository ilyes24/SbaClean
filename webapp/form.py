from Accounts.models import MyUser
from Address.models import *
from Post.models import *
from django import forms

from django.contrib.auth.forms import UserCreationForm

class UserRegistreForm(UserCreationForm):
    email=forms.EmailField()
    first_name=forms.CharField(required=True)
    last_name=forms.CharField(required=True)
    phone_number=forms.CharField(required=True)
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
    class Meta():
        model = Comment
        fields = ['description']    