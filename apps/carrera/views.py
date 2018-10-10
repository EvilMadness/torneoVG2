from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.carrera.forms import AddCarrera
from apps.carrera.models import Carrera
from sweetify.views import SweetifySuccessMixin


def index(request):
    return render(request, 'carrera/index.html')

class ShowCarrera(ListView):
    model = Carrera
    template_name = 'carrera/index.html'


class CreateCarrera(SweetifySuccessMixin, CreateView):
    model = Carrera
    form_class = AddCarrera
    template_name = 'carrera/add_carrera.html'
    sweetify_options = {'toast': True, 'position': 'top-left', 'timer': 3000}
    success_message = 'Carrera guardada correctamente'
    success_url = reverse_lazy('carrera:index')


class UpdateCarrera(SweetifySuccessMixin, UpdateView):
    model = Carrera
    form_class = AddCarrera
    template_name = 'carrera/add_carrera.html'
    sweetify_options = {'toast': True, 'position': 'top-left', 'timer': 3000}
    success_message = 'Carrera actualizada correctamente'
    success_url = reverse_lazy('carrera:index')


class DeleteCarrera(SweetifySuccessMixin, DeleteView):
    model = Carrera
    template_name = 'carrera/delete_carrera.html'
    sweetify_options = {'toast': True, 'position': 'top-left', 'timer': 3000}
    success_message = 'Carrera eliminada correctamente'
    success_url = reverse_lazy('carrera:index')


