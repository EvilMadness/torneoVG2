from django import forms

from apps.carrera.models import Carrera


class AddCarrera(forms.ModelForm):
    class Meta:
        model = Carrera

        fields = [
             'nombre_carrera'
        ]

        labels = {
            'nombre_carrera': 'Nombre de la carrera'
        }

        widgets = {
            'nombre_carrera' : forms.TextInput(attrs={'class': 'form-control'}),
        }
