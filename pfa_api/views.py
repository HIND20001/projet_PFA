from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from pfa_api.serializers import RecruteurSerializer, OffreSerializer
from pfa_api.models import Recruteur, Offre


# Create your views here.
#class RecruteurViewSet(viewsets.ModelViewSet):
# queryset = Recruteur.objects.all()
# serializer_class = RecruteurSerializer


class RecruteurListApiView(APIView):
   # add permission to check if user is authenticated
   #permission_classes = [permissions.IsAuthenticated]


   def get(self, request) :
            recruteur = Recruteur.objects.all()
            serializer = RecruteurSerializer(recruteur, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

   # 2. Create
   def post(self, request, *args, **kwargs):

         data = {
             'nom':request.data.get('nom'),
            'prenom':request.data.get('prenom'),
            'telephone':request.data.get('telephone'),
            'date_nais':request.data.get('date_nais'),
            'ville':request.data.get('ville'),
            'login':request.data.get('login'),
            'mdp':request.data.get('mdp'),
            'entreprise':request.data.get('entreprise'),
            'black_list':request.data.get('black_list'),
         }

         serializer = RecruteurSerializer(data=data)
         if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class RecruteurDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, todo_id):
        '''

        '''
        try:
            return Recruteur.objects.get(id=todo_id)
        except Recruteur.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, todo_id, *args, **kwargs):
        '''
        selecter un recruteur avec son id si il exist
        '''
        Recruteur_instance = self.get_object(todo_id)
        if not Recruteur_instance:
            return Response(
                {"res": "Object with recruteur id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = RecruteurSerializer(Recruteur_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, todo_id, *args, **kwargs):
        '''
         modifier un recruteur avec son id si il exist
        '''
        Recruteur_instance = self.get_object(todo_id)
        if not Recruteur_instance:
            return Response(
                {"res": "Object with Recruteur id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'nom': request.data.get('nom'),
            'prenom': request.data.get('prenom'),
            'telephone': request.data.get('telephone'),
            'date_nais': request.data.get('date_nais'),
            'ville': request.data.get('ville'),
            'login': request.data.get('login'),
            'mdp': request.data.get('mdp'),
            'entreprise': request.data.get('entreprise'),
            'black_list': request.data.get('black_list'),


        }
        serializer = RecruteurSerializer(instance = Recruteur_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, Recruteur_id, *args, **kwargs):
        '''
        Supprimer un recruteur avec son id si il exist
        '''
        Recruteur_instance = self.get_object(Recruteur_id, request.user.id)
        if not Recruteur_instance:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        Recruteur_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )

class OffreListApiView(APIView):
   # add permission to check if user is authenticated
   #permission_classes = [permissions.IsAuthenticated]


   def get(self, request) :
            offre =Offre.objects.all()
            serializer =OffreSerializer(offre, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

   # 2. Create
   def post(self, request, *args, **kwargs):

         data = {
             'recruteur': request.data.get('recruteur'),
             'annee_experience': request.data.get('annee_experience'),
             'connaissance': request.data.get('connaissance'),
             'contrat': request.data.get('contrat'),
             'critere': request.data.get('critere'),
             'formation': request.data.get('formation'),
             'mission': request.data.get('mission'),
             'nbr_a_recruter': request.data.get('nbr_a_recruter'),
             'salaire': request.data.get('salaire'),
             'tache_principale': request.data.get('tache_principale'),
             'langue': request.data.get('langue'),
             'specialite': request.data.get('specialite'),
             'ville': request.data.get('ville'),

         }

         serializer = OffreSerializer(data=data)
         if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)