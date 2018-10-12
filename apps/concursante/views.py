from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.concursante.forms import AddConcursante, EditConcursante
from apps.concursante.models import Concursante


def index(request):
    concursante = Concursante.objects.all()
    return render(request, 'concursante/index.html', {'object_list': concursante})


class ShowConcursantes(ListView):
    model = Concursante
    template_name = 'concursante/table.html'


class CreateConcursante(CreateView):
    model = Concursante
    form_class = AddConcursante
    template_name = 'concursante/add_concursante.html'
    success_url = reverse_lazy('concursante:index')


class UpdateConcursante(UpdateView):
    model = Concursante
    form_class = EditConcursante
    template_name = 'concursante/edit_concursante.html'
    success_url = reverse_lazy('concursante:index')


class DeleteConcursante(DeleteView):
    model = Concursante
    template_name = 'concursante/delete_concursante.html'
    success_url = reverse_lazy('concursante:index')