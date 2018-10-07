from django.urls import path
from apps.personaje.views import ShowPersonaje, DeletePersonaje, upload_file, UpdatePersonaje

app_name = 'personaje'

urlpatterns = [
    path('', ShowPersonaje.as_view(), name='index'),
    #path('add_personaje', CreatePersonaje.as_view(), name='add_personaje'),
    path('<int:pk>/edit_personaje', UpdatePersonaje.as_view(), name='edit_personaje'),
    path('<int:pk>/delete_personaje', DeletePersonaje.as_view(), name='delete_personaje'),
    path('add_personaje', upload_file, name="add_personaje"),
]