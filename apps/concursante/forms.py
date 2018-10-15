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
            'id_carrera',
            'id_escuela',
            'id_personaje',
        ]

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apaterno': forms.TextInput(attrs={'class': 'form-control'}),
            'amaterno': forms.TextInput(attrs={'class': 'form-control'}),
            'nickname': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'id_carrera': forms.Select(attrs={'class': 'form-control'}),
            'id_escuela': forms.Select(attrs={'class': 'form-control'}),
            'id_personaje': forms.Select(attrs={'class': 'form-control'}),
        }

class EditConcursante(forms.ModelForm):

    class Meta:
        model = Concursante

        fields = [
            'nombre',
            'apaterno',
            'amaterno',
            'nickname',
            'email',
            'id_carrera',
            'id_escuela',
            'id_personaje',
        ]

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apaterno': forms.TextInput(attrs={'class': 'form-control'}),
            'amaterno': forms.TextInput(attrs={'class': 'form-control'}),
            'nickname': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'id_carrera': forms.Select(attrs={'class': 'form-control'}),
            'id_escuela': forms.Select(attrs={'class': 'form-control'}),
            'id_personaje': forms.Select(attrs={'class': 'form-control'}),
        }