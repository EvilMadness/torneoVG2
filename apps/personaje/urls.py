from django.urls import path
from apps.personaje.views import ShowPersonaje, CreatePersonaje

app_name = 'personaje'

urlpatterns = [
    path('', ShowPersonaje.as_view(), name='index'),
    path('add_personaje', CreatePersonaje.as_view(), name='add_personaje'),
]