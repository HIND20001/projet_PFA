from rest_framework import serializers

from pfa_api.models import Recruteur,Offre

class RecruteurSerializer(serializers.ModelSerializer):
   class Meta:
       model = Recruteur
       fields = ('id', 'nom', 'prenom', 'telephone', 'date_nais', 'ville', 'login', 'mdp', 'entreprise', 'black_list')

class OffreSerializer(serializers.ModelSerializer):
   class Meta:
       model = Offre
       fields = '__all__'