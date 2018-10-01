from django.urls import path
from apps.carrera.views import index, ShowCarrera, CreateCarrera

app_name = 'carrera'

urlpatterns = [
    path('', ShowCarrera.as_view(), name='index'),
    path('add_carrera', CreateCarrera.as_view(), name='add_carrera'),
]