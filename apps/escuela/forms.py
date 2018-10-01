from django import forms

from apps.escuela.models import Escuela


class AddEscuela(forms.ModelForm):
    class Meta:
        model = Escuela

        fields = [
            'nombre',
            'municipio'
        ]

        widgets = {
            'nombre' : forms.TextInput(attrs={'class': 'form-control'}),
            'municipio' : forms.TextInput(attrs={'class': 'form-control'}),
        }
