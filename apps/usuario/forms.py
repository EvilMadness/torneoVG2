from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django.contrib.auth.models import User
from django import forms


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={
        'autofocus':True,
        'class': 'form_control',
        'placehorder': 'Nombre de usuario'
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
            'username',
            'first_name',
            'last_name',
            'email',
        ]

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }