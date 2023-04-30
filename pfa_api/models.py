from django.db import models

from django.db import models
class personne(models.Model):
        id=models.IntegerField
        nom=models.CharField(max_length=100)
        prenom=models.CharField(max_length=100)
        telephone=models.CharField(max_length=100)
        email=models.CharField(max_length=100)
        date_nais = models.DateTimeField()
        ville=models.CharField(max_length=100)
        login=models.CharField(max_length=100)
        mdp=models.CharField(max_length=100)


class Recruteur(personne):

    entreprise = models.CharField(max_length = 180)
    black_list = models.BooleanField(default=False)

class Langue(models.Model):
    id_langue =models.IntegerField
    langue =  models.CharField(max_length=100)

class Specialite(models.Model):
        id_specialite = models.IntegerField
        specialite = models.CharField(max_length=100)


class  Ville(models.Model):
    id_ville = models.IntegerField
    ville = models.CharField(max_length=100)

class Offre(models.Model):
        recruteur = models.ForeignKey(Recruteur, on_delete=models.CASCADE)
        id_offre = models.IntegerField
        annee_experience = models.IntegerField(max_length=100)
        connaissance = models.CharField(max_length=100)
        contrat = models.CharField(max_length=100)
        critere = models.CharField(max_length=100)
        formation = models.CharField(max_length=100)

        mission= models.CharField(max_length=100)
        nbr_a_recruter = models.IntegerField(max_length=100)
        salaire = models.FloatField(max_length=100)
        tache_principale = models.CharField(max_length=100)
        langue = models.ForeignKey(Langue, on_delete=models.CASCADE)
        specialite  = models.ForeignKey(Specialite , on_delete=models.CASCADE)
        ville = models.ForeignKey(Ville, on_delete=models.CASCADE)



