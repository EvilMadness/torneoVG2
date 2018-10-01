from django.urls import path
from apps.concursante.views import index, ShowConcursantes, CreateConcursante

app_name = 'concursante'

urlpatterns = [
    path('', index, name='index'),
    path('list', ShowConcursantes.as_view(), name='list'),
    path('add_concursante', CreateConcursante.as_view(), name='add_concursante'),
]
