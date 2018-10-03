from django.urls import path
from apps.home.views import index, logIn

app_name = 'home'

urlpatterns = [
    path('', index, name='index'),
    path('login', logIn, name='login'),
]