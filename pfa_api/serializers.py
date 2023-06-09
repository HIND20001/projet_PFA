from rest_framework import serializers

from pfa_api.models import Recruteur, Offre, Candidature,Candidat


class RecruteurSerializer(serializers.ModelSerializer):
   class Meta:
       model = Recruteur
       fields = '__all__'
class OffreSerializer(serializers.ModelSerializer):
   class Meta:
       model = Offre
       fields = '__all__'


class CandidatureSerializer(serializers.ModelSerializer):
   class Meta:
       model = Candidature
       fields = '__all__'

class candidatSerializer(serializers.ModelSerializer):
   class Meta:
       model = Candidat
       fields = '__all__'