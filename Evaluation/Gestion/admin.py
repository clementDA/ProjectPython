from django.contrib import admin
from .models import Projet,Tache,absence,Rapport,Utilisateur,Occupe
# Register your models here.


admin.site.register(Projet)
admin.site.register(Tache)
admin.site.register(absence)
admin.site.register(Rapport)
admin.site.register(Utilisateur)
admin.site.register(Occupe)

