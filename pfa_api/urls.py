
from django.urls import include, path





from .views import (
    RecruteurListApiView, RecruteurDetailApiView, OffreListApiView,
)


urlpatterns = [
    path('apiR', RecruteurListApiView.as_view()),
    path('apiR/<int:todo_id>/', RecruteurDetailApiView.as_view()),
    path('apiO', OffreListApiView.as_view()),]
