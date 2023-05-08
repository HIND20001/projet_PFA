
from django.urls import include, path





from .views import (
    OffreListApiView, RecruteurDetailApiView, OffreListApiView,
)


urlpatterns = [
    path('apiR', OffreListApiView.as_view()),
    path('apiR/<int:todo_id>/', RecruteurDetailApiView.as_view()),
    path('apiO', OffreListApiView.as_view()),]
