from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from apps.carrera.forms import AddCarrera
from apps.carrera.models import Carrera


def index(request):
    return render(request, 'carrera/index.html')

class ShowCarrera(ListView):
    model = Carrera
    template_name = 'carrera/index.html'


class CreateCarrera(CreateView):
    model = Carrera
    form_class = AddCarrera
    template_name = 'carrera/add_carrera.html'
    success_url = reverse_lazy('carrera:index')


class UpdateCarrera(UpdateView):
    model = Carrera
    form_class = AddCarrera
    template_name = 'carrera/add_carrera.html'
    success_url = reverse_lazy('carrera:index')