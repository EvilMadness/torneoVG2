from django.urls import path
from apps.concursante.views import index

app_name = 'concursante'

urlpatterns = [
    path('', index, name='index'),
]
