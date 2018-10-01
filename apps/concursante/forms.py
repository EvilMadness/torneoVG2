from django import forms

from apps.concursante.models import Concursante

class AddConcursante(forms.ModelForm):

    class Meta:
        model = Concursante

        fields = [
            'nombre',
            'apaterno',
            'amaterno',
            'nickname',
            'password',
            'email',
            'id_carrera',
            'id_escuela',
            'id_personaje',
        ]
        labels = {
            'nombre': 'Nombre',
            'apaterno': 'Apellido Paterno',
            'amaterno': 'Apellido Materno',
            'nickname': 'Nickname',
            'password': 'Contraseña',
            'email': 'Correo',
            'id_carrera': 'Carrera',
            'id_escuela': 'Escuela',
            'id_personaje': 'Personaje',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apaterno': forms.TextInput(attrs={'class': 'form-control'}),
            'amaterno': forms.TextInput(attrs={'class': 'form-control'}),
            'nickname': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'id_carrera': forms.Select(attrs={'class': 'form-control'}),
            'id_escuela': forms.Select(attrs={'class': 'form-control'}),
            'id_personaje': forms.Select(attrs={'class': 'form-control'}),
        }