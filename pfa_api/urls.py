
from django.urls import include, path





from .views import (
    RecruteurListApiView, RecruteurDetailApiView,
)


urlpatterns = [
    path('api', RecruteurListApiView.as_view()),
    path('api/<int:todo_id>/', RecruteurDetailApiView.as_view()),
]