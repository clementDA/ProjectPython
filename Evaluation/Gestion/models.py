from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
#Liste des modéles

#modéle utilisateur, réutilise les modele déjà existant des users
class Utilisateur(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    role = models.CharField(max_length=40)
    def __str__(self):
        return self.user.username


#modéle de représentation des projets
class Projet(models.Model):
    responsable=models.ForeignKey(Utilisateur,on_delete=models.CASCADE,null=True, blank=True)
    project_name = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    delivery_date= models.DateTimeField()
    project_statut =models.CharField( max_length=8,
        choices=(
            ("en pause", "En pause"),
            ("planifie", "Planifié"),
            ("en cours", "En cours"),
            ("livre", "Livré")          
        )
    )
    project_avancement = models.IntegerField(default=0)
    def __str__(self):
        return self.project_name
    #fonction de modification d'un projet
    def modifprojet(p_id,p_name,p_start_date,p_delivery_date,p_responsable):
        p_projet=Projet.objects.get(id=p_id)
        p_projet.name=p_name
        p_projet.start_date=p_start_date
        p_projet.delivery_date=p_delivery_date
        p_projet.responsable=p_responsable
        p_projet.save() 


#modéle de représentation des taches
class Tache(models.Model):
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE)
    tache_charge = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    tache_maitresse = models.ForeignKey("self",null=True, on_delete=models.CASCADE)
    tache_name = models.CharField(max_length=200)
    tache_description = models.CharField(max_length=200)
    tache_priorite=models.IntegerField()
    start_date= models.DateTimeField()
    tache_duree=models.IntegerField()
    tache_statut =models.CharField( max_length=8,
        choices=(
            ("en pause", "En pause"),
            ("planifié", "Planifié"),
            ("en cours", "En cours"),
            ("validee", "Validée"),
            ("livré", "Livré")          
        )
    )
    tache_etat = models.IntegerField()
    tache_niveau= models.IntegerField()
    def __str__(self):
        return self.tache_name


#modéle de présentation des rapports
class Rapport(models.Model):
    tache = models.ForeignKey(Tache, on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    rapport_date= models.DateTimeField()
    rapport_description= models.CharField(max_length=200)
    def __str__(self):
        return self.rapport_description
    def addrapport(tacheid,utilisateur,description):
         newrapport=Rapport(tache =tacheid,utilisateur=utilisateur, rapport_date=timezone.now() ,rapport_description=description )
         newrapport.save()


#modéle de sauvegarde des absences
class absence(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    start_date= models.DateTimeField()
    end_date= models.DateTimeField()
    absence_raison = models.CharField(max_length=30)
    def __str__(self):
        return self.absence_raison


#modéle d'attribution des utilisateurs aux taches
class Occupe(models.Model):
     utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
     tache = models.ForeignKey(Tache, on_delete=models.CASCADE)
