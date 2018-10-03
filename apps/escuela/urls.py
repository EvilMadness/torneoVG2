from django.urls import path
from apps.escuela.views import ShowEscuela, CreateEscuela, UpdateEscuela, DeleteEscuela

app_name = 'escuela'

urlpatterns = [
    path('', ShowEscuela.as_view(), name='index'),
    path('add_escuela', CreateEscuela.as_view(), name='add_escuela'),
    path('<int:pk>/edit_escuela', UpdateEscuela.as_view(), name='edit_escuela'),
    path('<int:pk>/delete_escuela', DeleteEscuela.as_view(), name='delete_escuela'),
]