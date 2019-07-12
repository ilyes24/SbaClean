from Address.models import *
from Post.models import *
from django import forms


class PostForm(forms.ModelForm):
    title = forms.CharField(label='Title', max_length=255)
    description = forms.CharField(label='Description', max_length=255)
    city=forms.ModelChoiceField(queryset=City.objects.all())
    longitude = forms.CharField(label='Longitude', max_length=255)
    latitude = forms.CharField(label='Latitude', max_length=255)
    image = forms.CharField(label='Image', max_length=255)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
    class Meta:
        model=Post
        fields=['title','description','city','longitude','latitude','image']
