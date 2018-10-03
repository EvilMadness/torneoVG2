from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django import forms
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={
        'autofocus':True,
        'class':'form_control',
        'placehorder':'Nombre de usuario'
    }))
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class':'form_control',
            'placehorder':'Contraseña'
        }),
    )


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