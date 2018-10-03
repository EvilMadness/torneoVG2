from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.escuela.forms import AddEscuela
from apps.escuela.models import Escuela


def index(request):
    return render(request, 'escuela/index.html')


class ShowEscuela(ListView):
    model = Escuela
    template_name = 'escuela/index.html'


class CreateEscuela(CreateView):
    model = Escuela
    form_class = AddEscuela
    template_name = 'escuela/add_escuela.html'
    success_url = reverse_lazy('escuela:index')


class UpdateEscuela(UpdateView):
    model = Escuela
    form_class = AddEscuela
    template_name = 'escuela/add_escuela.html'
    success_url = reverse_lazy('escuela:index')


class DeleteEscuela(DeleteView):
    model = Escuela
    template_name = 'escuela/delete_escuela.html'
    success_url = reverse_lazy('escuela:index')
