from django.urls import path
from apps.personaje.views import ShowPersonaje, CreatePersonaje, DeletePersonaje

app_name = 'personaje'

urlpatterns = [
    path('', ShowPersonaje.as_view(), name='index'),
    path('add_personaje', CreatePersonaje.as_view(), name='add_personaje'),
    path('<int:pk>/delete_personaje', DeletePersonaje.as_view(), name='delete_personaje'),
]