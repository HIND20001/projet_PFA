from django.contrib import admin
from .models import Candidat, Recruteur, Offre, Ville, Langue, Specialite, Diplome, Candidature

# Register your models here.
admin.site.register(Candidat)
admin.site.register(Recruteur)
admin.site.register(Offre)
admin.site.register(Ville)
admin.site.register(Langue)
admin.site.register(Specialite)
admin.site.register(Diplome)
admin.site.register(Candidature)
