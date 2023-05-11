
from django.urls import include, path





from .views import (
    OffreListApiView, OffreListApiView, OffreDetailApiView, RecruteurListApiView, RecruteurDetailApiView,
)


urlpatterns = [
    path('apiO', OffreListApiView.as_view()),
    path('apiO/<int:todo_id>/', OffreDetailApiView.as_view()),
    path('apiR', RecruteurListApiView.as_view()),
    path('apiR/<int:todo_id>/', RecruteurDetailApiView.as_view()),
    ]
