# Generated by Django 5.0.3 on 2024-04-02 19:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Projet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=200)),
                ('start_date', models.DateTimeField()),
                ('delivery_date', models.DateTimeField()),
                ('project_statut', models.CharField(choices=[('en pause', 'En pause'), ('planifie', 'Planifié'), ('en cours', 'En cours'), ('livre', 'Livré')], max_length=8)),
                ('project_avancement', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=40)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tache',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tache_name', models.CharField(max_length=200)),
                ('tache_description', models.CharField(max_length=200)),
                ('tache_priorite', models.IntegerField()),
                ('start_date', models.DateTimeField()),
                ('tache_duree', models.IntegerField()),
                ('tache_statut', models.CharField(choices=[('en pause', 'En pause'), ('planifié', 'Planifié'), ('en cours', 'En cours'), ('validee', 'Validée'), ('livré', 'Livré')], max_length=8)),
                ('tache_etat', models.IntegerField()),
                ('tache_niveau', models.IntegerField()),
                ('projet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion.projet')),
                ('tache_charge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion.utilisateur')),
            ],
        ),
        migrations.CreateModel(
            name='Rapport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rapport_date', models.DateTimeField()),
                ('rapport_description', models.CharField(max_length=200)),
                ('tache', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion.tache')),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion.utilisateur')),
            ],
        ),
        migrations.CreateModel(
            name='Occupe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tache', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion.tache')),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion.utilisateur')),
            ],
        ),
        migrations.CreateModel(
            name='absence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('absence_raison', models.CharField(max_length=30)),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion.utilisateur')),
            ],
        ),
    ]
