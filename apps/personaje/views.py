from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView

from apps.personaje.forms import AddPersonaje
from apps.personaje.models import Personaje


def index(request):
    return render(request, 'personaje/index.html')

class ShowPersonaje(ListView):
    model = Personaje
    template_name = 'personaje/index.html'

class CreatePersonaje(CreateView):
    model = Personaje
    form_class = AddPersonaje
    template_name = 'personaje/add_personaje.html'
    success_url = reverse_lazy('personaje:index')


class DeletePersonaje(DeleteView):
    model = Personaje
    template_name = 'personaje/delete_personaje.html'
    success_url = reverse_lazy('personaje:index')