from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.loging, name="login"),
    path("logingout", views.logingout, name="logingout"),
    path("projet/<int:project_id>", views.projet, name="projet"),
    path("tache/<int:tache_id>", views.tache, name="tache"),
    path("ajoutrapport/<int:tache_id>", views.ajoutrapport, name="ajoutrapport"),
    path("modprojet/<int:project_id>", views.modprojet, name="modprojets"),

]