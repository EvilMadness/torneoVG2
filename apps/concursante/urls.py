from django.urls import path
from apps.concursante.views import index, ShowConcursantes, CreateConcursante, UpdateConcursante, DeleteConcursante

app_name = 'concursante'

urlpatterns = [
    path('', index, name='index'),
    path('list', ShowConcursantes.as_view(), name='list'),
    path('add_concursante', CreateConcursante.as_view(), name='add_concursante'),
    path('<int:pk>/edit_concursante', UpdateConcursante.as_view(), name='edit_concursante'),
    path('<int:pk>/delete_concursante', DeleteConcursante.as_view(), name='delete_concursante'),
]
