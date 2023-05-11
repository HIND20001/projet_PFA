from django.db import models

from django.db import models
from django.contrib.auth.models import User


class Personne(models.Model):
    nom = models.CharField(max_length = 180)
    prenom= models.CharField(max_length = 180)
    telephone= models.CharField(max_length = 180)
    date_nais= models.DateTimeField
    ville= models.CharField(max_length = 180)
    login= models.CharField(max_length = 180)
    mdp= models.CharField(max_length = 180)

    black_list=models.BooleanField
    class meta:
        abstract=True


class Recruteur(Personne):
    entreprise= models.CharField(max_length = 180)
class Ville(models.Model)    :
    nom_ville = models.CharField(max_length=180)

class Langue(models.Model)    :
    nom_langue = models.CharField(max_length=180)

class Specialite(models.Model)    :
    nom_specialite = models.CharField(max_length=180)
class Diplome(models.Model)    :
    nom_diplome = models.CharField(max_length=180)


class Offre(models.Model):

        Recruteur = models.ForeignKey(Recruteur, on_delete=models.CASCADE , default='1')
        annee_experience = models.IntegerField
        connaissance = models.CharField(max_length=180)
        contrat = models.CharField(max_length=180)
        critere = models.CharField(max_length=180)
        experience_requete = models.CharField(max_length=180)
        formation = models.CharField(max_length=180)
        mission = models.CharField(max_length=180)
        nbr_a_recruter = models.IntegerField
        salaire = models.FloatField
        tache_principale= models.CharField(max_length=180)
        Langue = models.ForeignKey(Langue, on_delete=models.CASCADE, default=None)
        Ville = models.ForeignKey(Ville, on_delete=models.CASCADE, default=None)
        Specialite = models.ForeignKey(Specialite, on_delete=models.CASCADE, default=None)

class Candidat(Personne):
    AnneDiplome = models.IntegerField(default='null')
    DernierPostOccupe = models.CharField(max_length=180,default='null')
    ecole = models.CharField(max_length=180,default='null')
    NbrAnnance = models.IntegerField(default='null')
    NbrAnnanceExp = models.IntegerField(default='null')
    black_list = models.BooleanField(default='null')

class Candidature(models.Model):
    Offre_id = models.ForeignKey(Offre, on_delete=models.CASCADE, default='1')
    annee_diplome = models.IntegerField
    date_postulation = models.DateTimeField
    Dernier_post_occupe = models.CharField(max_length=180)
    NbrAnneeExperience = models.IntegerField
    Diplome = models.ForeignKey(Diplome, on_delete=models.CASCADE, default=None)
    Statut_candidature = models.IntegerField

