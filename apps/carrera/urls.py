from django.urls import path
from apps.carrera.views import index, ShowCarrera, CreateCarrera, UpdateCarrera

app_name = 'carrera'

urlpatterns = [
    path('', ShowCarrera.as_view(), name='index'),
    path('add_carrera', CreateCarrera.as_view(), name='add_carrera'),
    path('<int:pk>/edit_carrera', UpdateCarrera.as_view(), name='edit_carrera'),
]