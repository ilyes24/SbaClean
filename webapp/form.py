from Accounts.models import MyUser
from Address.models import *
from django import forms

from django.contrib.auth.forms import UserCreationForm

class UserRegistreForm(UserCreationForm):
    email=forms.EmailField()
    First_name=forms.CharField(required=True)
    Last_name=forms.CharField(required=True)
    phone_number=forms.CharField(max_length=13,required=True)
    Address=forms.CharField(required=True) 
    City=forms.ChoiceField(choices=[(City.id, City.name) for City in City.objects.all()])
   
    class Meta:
        model=MyUser
        fields=['username','email','First_name','Last_name','phone_number','Address','City','password1','password2']
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = MyUser
        fields = ['username','password']       