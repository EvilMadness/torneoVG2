from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from apps.concursante.forms import AddConcursante
from apps.concursante.models import Concursante


def index(request):
    return render(request, 'concursante/index.html')


class ShowConcursantes(ListView):
    model = Concursante
    template_name = 'concursante/table.html'


class CreateConcursante(CreateView):
    model = Concursante
    form_class = AddConcursante
    template_name = 'concursante/add_concursante.html'
    success_url = reverse_lazy('concursante:index')