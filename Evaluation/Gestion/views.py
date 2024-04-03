from django.shortcuts import render, redirect
from .models import Projet,Tache,absence,Rapport,Utilisateur,Occupe
from django.contrib.auth import authenticate,login,logout
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone


def index(request):
   listprojet=Projet.objects.all()      
   context = {"listprojet": listprojet}
   return render(request, "Gestion/index.html", context)
   


def loging(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            listprojet=Projet.objects.all()      
            context = {"listprojet": listprojet}
            return render(request, "Gestion/index.html", context)
        else:
          return render(request, "Gestion/log.html")
    else:
         return render(request, "Gestion/log.html")
    
       
def logingout(request):
    logout(request)
    return redirect('login')

def projet(request,project_id):
    projet=Projet.objects.get(pk=project_id)
    taches=Tache.objects.filter(projet=project_id).order_by('tache_priorite')
    return render(request, "Gestion/projet.html", {"Projet": projet,"Tache": taches})

def tache(request,tache_id):
    tache=Tache.objects.get(pk=tache_id)
    rapport=Rapport.objects.filter(tache=tache_id).order_by('rapport_date')
    return render(request, "Gestion/tache.html", {"Tache": tache, "Rapport": rapport})



def ajoutrapport(request,tache_id):
    if request.method == "POST":
         utilisateur=Utilisateur.objects.get(pk=request.POST['utilisateur_id'])
         newrapport=Rapport(tache =Tache.objects.get(pk=tache_id),utilisateur=utilisateur, rapport_date=timezone.now() ,rapport_description=request.POST['description'] )
         newrapport.save()
         tache=Tache.objects.get(pk=tache_id)
         rapport=Rapport.objects.filter(tache=tache_id).order_by('rapport_date')
         return render(request, "Gestion/tache.html", {"Tache": tache, "Rapport": rapport})
    else:
        tache=Tache.objects.get(pk=tache_id)
        return render(request, "Gestion/ajoutrapport.html", {"Tache": tache})


def modprojet(request,project_id):
    projet=Projet.objects.get(pk=project_id)
    taches=Tache.objects.filter(projet=project_id).order_by('tache_priorite')
    return render(request, "Gestion/modprojet.html", {"Projet": projet})