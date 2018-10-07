from django import forms

from apps.personaje.models import Personaje


class AddPersonaje(forms.ModelForm):
    class Meta:
        model = Personaje

        fields = [
            'nombre',
            'imagen'
        ]

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
        }


class UploadForm(forms.Form):
    filename = forms.CharField(max_length=100)
    docfile = forms.FileField(label='Selecciona un archivo')
