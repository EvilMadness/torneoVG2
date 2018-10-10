from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from apps.personaje.forms import AddPersonaje, UploadForm
from apps.personaje.models import Personaje


def index(request):
    return render(request, 'personaje/index.html')


class ShowPersonaje(ListView):
    model = Personaje
    template_name = 'personaje/index.html'
    paginate_by = 5


#class CreatePersonaje(CreateView):
#   model = Personaje
#    form_class = AddPersonaje
#    template_name = 'personaje/add_personaje.html'
#    success_url = reverse_lazy('personaje:index')


class UpdatePersonaje(UpdateView):
    model = Personaje
    form_class = AddPersonaje
    template_name = 'personaje/add_personaje.html'
    success_url = reverse_lazy('personaje:index')



class DeletePersonaje(DeleteView):
    model = Personaje
    template_name = 'personaje/delete_personaje.html'
    success_url = reverse_lazy('personaje:index')


def upload_file(request):
    if request.method == 'POST':
        form = AddPersonaje(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Personaje(nombre=request.POST['nombre'], imagen=request.FILES['imagen'])
            newdoc.save(form)
            return redirect("personaje:index")
    else:
        form = AddPersonaje()
    #tambien se puede utilizar render_to_response
    #return render_to_response('upload.html', {'form': form}, context_instance = RequestContext(request))
    return render(request, 'personaje/add_personaje.html', {'form': form})