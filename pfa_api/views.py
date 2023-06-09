from django.db.models import Q
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pfa_api.models import Recruteur, Offre, Candidature, Candidat
from .serializers import OffreSerializer, RecruteurSerializer, CandidatureSerializer, candidatSerializer
from rest_framework import permissions
from rest_framework.decorators import action


class OffreListApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all

    def get(self, request, *args, **kwargs):
        '''
        List all the Offre items
        '''
        Offres = Offre.objects.all()
        serializer = OffreSerializer(Offres, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Offre with given Offre data
        '''
        data = {
            'Recruteur': request.Recruteur.id,

            'annee_experience': request.data.get('annee_experience'),
            'connaissance': request.data.get('connaissance'),
            'contrat': request.data.get('contrat'),
            'critere': request.data.get('critere'),
            'experience_requete': request.data.get('experience_requete'),
            'formation': request.data.get('formation'),
            'mission': request.data.get('mission'),
            'nbr_a_recruter': request.data.get('nbr_a_recruter'),
            'salaire': request.data.get('salaire'),
            'tache_principale': request.data.get('tache_principale'),
            'Langue': request.data.get('Langue'),
            'Ville': request.data.get('Ville'),
            'Specialite': request.data.get('Specialite'),
        }
        serializer = OffreSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OffreDetailApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    def get_Offre(self, Offre_id):
        '''
        Helper method to get the object offre  with given offre_id
        '''
        try:
            return Offre.objects.get(id=Offre_id)
        except Offre.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, r_id, *args, **kwargs):
        '''
        Retrieves the Offre with given Recruteur_id
        '''
        Offres = Offre.objects.filter(Recruteur_id=r_id)
        serializer = OffreSerializer(Offres, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update

    def put(self, request, Offre_id, *args, **kwargs):
        '''
        Updates the todo item with given todo_id if exists
        '''
        Offre_instance = self.get_object(Offre_id)
        if not Offre_instance:
            return Response(
                {"res": "Object with Offre_id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'Recruteur': request.Recruteur.id,

            'annee_experience': request.data.get('annee_experience'),
            'connaissance': request.data.get('connaissance'),
            'contrat': request.data.get('contrat'),
            'critere': request.data.get('critere'),
            'experience_requete': request.data.get('experience_requete'),
            'formation': request.data.get('formation'),
            'mission': request.data.get('mission'),
            'nbr_a_recruter': request.data.get('nbr_a_recruter'),
            'salaire': request.data.get('salaire'),
            'tache_principale': request.data.get('tache_principale'),
            'Langue': request.data.get('Langue'),
            'Ville': request.data.get('Ville'),
            'Specialite': request.data.get('Specialite'),
        }
        serializer = OffreSerializer(
            instance=Offre_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, Offre_id, *args, **kwargs):
        '''
        Deletes the Offre item with given Offre_id if exists
        '''
        Offre_instance = self.get_object(Offre_id)
        if not Offre_instance:
            return Response(
                {"res": "Object with Offre id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        Offre_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )


class RecruteurListApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all

    def get(self, request, *args, **kwargs):
        '''
        List all the Recruteur items
        '''
        Recruteurs = Recruteur.objects.all()
        serializer = RecruteurSerializer(Recruteurs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Recruteur with given Recruteur data
        '''
        data = {
            'Recruteur': request.Recruteur.id,

            'nom': request.data.get('nom'),
            'prenom': request.data.get('prenom'),
            'telephone': request.data.get('telephone'),
            'date_nais': request.data.get('date_nais'),
            'ville': request.data.get('ville'),
            'login': request.data.get('login'),
            'mdp': request.data.get('mdp'),
            'black_list': request.data.get('black_list'),
            'entreprise': request.data.get('entreprise'),

        }
        serializer = RecruteurSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RecruteurDetailApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]
    def get_Recruteur(self, Offre_id):
        '''
        Helper method to get the object offre  with given Recruteur_id
        '''
        try:
            return Offre.objects.get(id=Offre_id)
        except Offre.DoesNotExist:
            return None

    # 4. Update

    def put(self, request, Recruteur_id, *args, **kwargs):
        '''
        Updates the Recruteur item with given Recruteur_id if exists
        '''
        Recruteur_instance = self.get_object(Recruteur_id)
        if not Recruteur_instance:
            return Response(
                {"res": "Object with Offre_id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'Recruteur': request.Recruteur.id,

            'annee_experience': request.data.get('annee_experience'),
            'connaissance': request.data.get('connaissance'),
            'contrat': request.data.get('contrat'),
            'critere': request.data.get('critere'),
            'experience_requete': request.data.get('experience_requete'),
            'formation': request.data.get('formation'),
            'mission': request.data.get('mission'),
            'nbr_a_recruter': request.data.get('nbr_a_recruter'),
            'salaire': request.data.get('salaire'),
            'tache_principale': request.data.get('tache_principale'),
            'Langue': request.data.get('Langue'),
            'Ville': request.data.get('Ville'),
            'Specialite': request.data.get('Specialite'),
        }
        serializer = RecruteurSerializer(
            instance=Recruteur_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, Recruteur_id, *args, **kwargs):
        '''
        Deletes the Offre item with given Offre_id if exists
        '''
        Recruteur_instance = self.get_object(Recruteur_id)
        if not Recruteur_instance:
            return Response(
                {"res": "Object with Offre id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        Recruteur_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )

    def getCan(self, request, O_id, *args, **kwargs):
        '''
        Retrieves the Offre with given Recruteur_id
        '''
        Candidatures = Candidature .objects.filter(Offre_id=O_id)
        serializer = CandidatureSerializer(Candidatures, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class candidatListApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all

    def get(self, request, *args, **kwargs):
        '''
        List all the candidat items
        '''
        candidats = Candidat.objects.all()
        serializer = candidatSerializer(candidats, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the candidat with given candidat data
        '''
        serializer = candidatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class candidatDetailApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    def get_object(self, candidat_id):
        '''
        Helper method to get the object candidat with given candidat_id
        '''
        try:
            return Candidat.objects.get(id=candidat_id)
        except Candidat.DoesNotExist:
            return None

    def get(self, request, candidat_id, *args, **kwargs):
        '''
        Retrieves the candidat with given candidat_id
        '''
        candidat_instance = self.get_object(candidat_id)
        if not candidat_instance:
            return Response(
                {"res": "Object with candidat_id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = candidatSerializer(candidat_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, candidat_id, *args, **kwargs):
        '''
        Updates the candidat item with given candidat_id if exists
        '''
        candidat_instance = self.get_object(candidat_id)
        if not candidat_instance:
            return Response(
                {"res": "Object with candidat_id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'AnneDiplome': request.data.get('AnneDiplome'),
            'Diplome': request.data.get('Diplome'),
            'ecole': request.data.get('ecole'),
            'NbrAnnance': request.data.get('NbrAnnance'),
            'NbrAnneeExp': request.data.get('NbrAnneeExp'),
            'black_list': request.data.get('black_list'),
        }
        serializer = candidatSerializer(
            instance=candidat_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, candidat_id, *args, **kwargs):
        '''
        Deletes the candidat item with given candidat_id if exists
        '''
        candidat_instance = self.get_object(candidat_id)
        if not candidat_instance:
            return Response(
                {"res": "Object with candidat id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        candidat_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )


class candidatureListApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all

    def get(self, request, *args, **kwargs):
        '''
        List all the candidature items
        '''
        candidatures = Candidature.objects.all()
        serializer = CandidatureSerializer(candidatures, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the candidature with given candidature data
        '''
        serializer = CandidatureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class candidatureDetailApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    def get_object(self, candidature_id):
        '''
        Helper method to get the object candidature with given candidature_id
        '''
        try:
            return Candidature.objects.get(id=candidature_id)
        except Candidature.DoesNotExist:
            return None

    def get(self, request, candidature_id, *args, **kwargs):
        '''
        Retrieves the candidature with given candidature_id
        '''
        candidature_instance = self.get_object(candidature_id)
        if not candidature_instance:
            return Response(
                {"res": "Object with candidature_id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = CandidatureSerializer(candidature_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, candidature_id, *args, **kwargs):
        '''
        Updates the candidature item with given candidature_id if exists
        '''
        candidature_instance = self.get_object(candidature_id)
        if not candidature_instance:
            return Response(
                {"res": "Object with candidature_id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'Offre': request.data.get('Offre'),
            'Dernier_post_occupe': request.data.get('Dernier_post_occupe'),
            'Diplome': request.data.get('Diplome'),
        }
        serializer = CandidatureSerializer(
            instance=candidature_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, candidature_id, *args, **kwargs):
        '''
        Deletes the candidature item with given candidature_id if exists
        '''
        candidature_instance = self.get_object(candidature_id)
        if not candidature_instance:
            return Response(
                {"res": "Object with candidature id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        candidature_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
