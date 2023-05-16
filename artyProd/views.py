from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserRegistrationForm,updateProfile,ajouteEquipe,ajouteProjet,updateProjet,ajoutContact
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.shortcuts import redirect

from .models import *
# Create your views here.
def home(request):
    return render(request,'artyProd/home.html') 
def index(request):
    service=Service.objects.all()
    equipe=Equipe.objects.all()
    if request.method == "POST":
        form = ajoutContact(request.POST)
        context={'form':form,'Service':service,'equipe':equipe}
        if form.is_valid():
            form.save()
    else :  
        form = ajoutContact()     
        context={'form':form,'Service':service,'equipe':equipe}
    return render(request,'artyProd/internaute.html',context)
def register(request):
    if request.method == 'POST' :
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            Personnel.objects.create(
                user=user,
                nom=username
            )
            login(request,user)
            messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')
            return redirect('home')
    else :
        form = UserRegistrationForm()
    return render(request,'registration/register.html',{'form' : form})   
def settings(request):
    personnel=request.user.personnel
    form=updateProfile(instance=personnel)
    if request.method == 'POST':
        form=updateProfile(request.POST,request.FILES, instance=personnel)
        if form.is_valid():
          form.save()
    context={'form':form}
    return render(request,'artyProd/settings.html',context)
def ajoutequipe(request):
    if request.method == "POST" :
        form = ajouteEquipe(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'artyProd/home.html',{'form':form,'msg5':'la methode d ajout est terminer'})
    else :
         form =ajouteEquipe()
    return render(request,'artyProd/equipe.html',{'form':form})
def utilisateur(request):
    personnel=Personnel.objects.all()
    return render(request,'artyProd/utilisateur.html',{'personne':personnel})
def ajoutProjet(request,id):
    personne=Personnel.objects.filter(user_id=id)
    if request.method == "POST":
        form = ajouteProjet(request.POST,request.FILES)
        context={'form':form,'personne':personne}
        if form.is_valid():
            form.save()
    else :
         form =ajouteProjet()
         context={'form':form,'personne':personne}
    return render(request,'artyProd/ajoutProjet.html',context)
def listProjet(request,id):
    personne=Personnel.objects.filter(user_id=id)
    return render(request,'artyProd/projet.html',{'personne':personne})
def achevee(request,id):
    personne=Projett.objects.filter(Equipe=id)
    return render(request,'artyProd/listprojet.html',{'personne':personne,'titel':'o'})
def encour(request,id):
    personne=Projett.objects.filter(Equipe=id)
    return render(request,'artyProd/Encour.html',{'personne':personne,'titel':'n'})
def updateProjet(request,id):
    personnel=Projett.objects.get(id=id)
    form=ajouteProjet(instance=personnel)
    if request.method == 'POST':
        form=ajouteProjet(request.POST,request.FILES, instance=personnel)
        if form.is_valid():
          form.save()
          return redirect('/artyProd')
    context={'form':form}
    return render(request,'artyProd/updateprojet.html',context)
def detletProj(request,id):
    projet=Projett.objects.get(id=id)
    projet.delete()
    return render(request,'artyProd/home.html',{'msg5':'la methode de supression est terminer'})
def detaisService(request,id):
    products=Projett.objects.filter(Service_id=id)
    context={'products':products,'msg2':"VOILA LA LISTE DE PROJET"}
    return render(request,'artyProd/details.html',context)
def detailProj(request,pk):
    details=Projett.objects.filter(id=pk)
    context={'details':details}
    return render(request,'artyProd/detailsProj.html',context)
def detailTeam(request,pk):
    personne=Personnel.objects.filter(Equipe_id=pk)
    context={'personne':personne,'msg':"NOTRE ÉQUIPE INCROYABLE",'msg1':"Ils est composer par :"}
    return render(request,'artyProd/details.html',context)
def listContact(request):
    contact=Contact.objects.all()
    context={'contact':contact}
    return render(request,'artyProd/listeContact.html',context)
def supContact(request,pk):
    sup=Contact.objects.get(id=pk)
    sup.delete()
    return redirect('/artyProd/listContact')
def listProjete(request):
    personne=Projett.objects.all()
    return render(request,'artyProd/adminProjet.html',{'personne':personne})
def listeEquipe(request):
    personne=Equipe.objects.all()
    return render(request,'artyProd/listeEquipe.html',{'personne':personne})
def detletEquipe(request,pk):
    projet=Equipe.objects.get(id=pk)
    projet.delete()
    return render(request,'artyProd/home.html',{'msg5':'la methode de supression est terminer'})
