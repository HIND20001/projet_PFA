
from django.urls import include, path


from .views import OffreListApiView, OffreListApiView, OffreDetailApiView, RecruteurListApiView, RecruteurDetailApiView, candidatListApiView, candidatDetailApiView, candidatureListApiView,candidatureDetailApiView


urlpatterns = [
    path('apiO', OffreListApiView.as_view()),
    path('apiO/<int:todo_id>/', OffreDetailApiView.as_view()),
    path('apiR', RecruteurListApiView.as_view()),
    path('apiR/<int:todo_id>/', RecruteurDetailApiView.as_view()),
    path('candidats/', candidatListApiView.as_view()),
    path('candidats/<int:candidat_id>', candidatDetailApiView.as_view()),
    path('candidatures/', candidatureListApiView.as_view()),
    path('candidatures/<int:candidature_id>', candidatureDetailApiView.as_view()),

]
