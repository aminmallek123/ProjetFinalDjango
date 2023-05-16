from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index,name='home'),
    path('/index', views.home,name='index'),
    path('register/',views.register, name = 'register'),
    path('settigns/',views.settings, name = 'settigns'), 
    path('ajoutEquipe/',views.ajoutequipe, name = 'equipe'),
    path('listUser/',views.utilisateur, name = 'user'),
    path('ajoutProjet/<int:id>',views.ajoutProjet, name = 'projet'),
    path('ListeProjet/<int:id>',views.listProjet, name = 'List'),
    path('acheve/<int:id>',views.achevee, name = 'List'),
    path('encour/<int:id>',views.encour, name = 'encour'),
    path('updateProjet/<int:id>',views.updateProjet, name = 'Modifierprojet'),
    path('deleteProjet/<int:id>',views.detletProj, name = 'detletProj'),
    path('detailsServise/<int:id>',views.detaisService, name = 'detaisService'),
    path('Art/<int:pk>',views.detailProj, name = 'detailProj'),
    path('team/<int:pk>',views.detailTeam, name = 'detailProj'),
     path('contact/<int:pk>',views.supContact, name = 'suprimer'),
    path('listContact/',views.listContact, name = 'contact'),
    path('projetListe/',views.listProjete, name = 'listProjet'),
    path('equipeListe/',views.listeEquipe, name = 'listeEquipe'),
    path('deletEquipe/<int:pk>',views.detletEquipe, name = 'detletEquipe'),
]
