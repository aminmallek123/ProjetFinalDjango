from django.db import models
from datetime import datetime 
from django.contrib.auth.models import User
# Create your models here.
class Personnel(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    nom=models.CharField(max_length=100)
    fichier_cv=models.FileField(upload_to='photos')
    fichier_photo=models.FileField(default="user.png",upload_to='photos')
    lien_prv=models.TextField()
    Equipe=models.ForeignKey('Equipe',on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.nom+' '+self.lien_prv
class Service(models.Model):
    type=models.CharField(max_length=100)
    decription=models.TextField()
    def __str__(self):
        return self.type    
class Equipe(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name     
class Projet(models.Model):
    libellai=models.CharField(max_length=100)
    description=models.TextField()
    date_debut=models.DateTimeField(default=datetime.now(), blank=True)
    date_fin= models.DateField(null=True, blank=True)
    acheve=models.CharField(max_length=1)
    fichier=models.FileField(upload_to='photos')
    Service=models.ForeignKey('Service',on_delete=models.CASCADE,null=True)
    Equipe=models.CharField(max_length=25)
    def __str__(self):
        return self.libellai+' '+self.description+' '+self.acheve    
class Projett(models.Model):
    libellai=models.CharField(max_length=100)
    description=models.TextField()
    date_debut=models.DateTimeField(default=datetime.now(), blank=True)
    date_fin= models.DateField(null=True,blank=True)
    acheve=models.CharField(max_length=1)
    fichier=models.FileField(upload_to='photos')
    Service=models.ForeignKey('Service',on_delete=models.CASCADE,null=True)
    Equipe=models.CharField(max_length=25)
    pdf=models.FileField(upload_to='fichier')
    def __str__(self):
        return self.libellai+' '+self.description+' '+self.acheve
class Contact(models.Model):
    Name=models.CharField(max_length=20)
    Email=models.CharField(max_length=30)
    phone=models.CharField(max_length=20)
    msg=models.TextField(max_length=20)
    def __str__(self):
        return self.Name+';'+self.Email+';'+self.phone+";"+self.msg         
     