from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='Prénom')
    last_name = forms.CharField(label='Nom')
    email = forms.EmailField(label='Adresse e-mail')
class Meta(UserCreationForm.Meta):
    model = User
    fields = UserCreationForm.Meta.fields + ('first_name', 'last_name' , 'email')
class updateProfile(ModelForm):
    class Meta:
        model=Personnel
        fields = "__all__"
        exclude=['user']  
class ajouteEquipe(ModelForm):
    class Meta:
        model=Equipe
        fields = "__all__"
class ajouteProjet(ModelForm):
    class Meta:
        model=Projett
        fields = "__all__"
class updateProjet(ModelForm):
    class Meta:
        model=Projett
        fields = "__all__" 
class ajoutContact(ModelForm):
    Name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'})) 
    Email= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'})) 
    phone= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'})) 
    msg= forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'})) 
    class Meta:
        model=Contact
        fields = "__all__"                
                    