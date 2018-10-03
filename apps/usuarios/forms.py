from django import forms
from django.contrib.auth.forms import UserCreationForm

from apps.usuarios.models import User

class AddUser(UserCreationForm):

    class Meta:
        model = User

        fields = [
            'password',
            'username',
            'first_name',
            'last_name',
            'email',
        ]

        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }