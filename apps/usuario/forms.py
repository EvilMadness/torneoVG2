from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth import password_validation
from apps.usuario.models import User
from django import forms
from apps.usuario.backends import CustomBackendUser as Auth


class ResetForm(PasswordResetForm):
    email = forms.EmailField(max_length=254, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Correo electrónico'
    }))


class ResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nueva contraseña'
        }),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirmar contraseña'
        }),
    )


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={
        'autofocus': True,
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
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username is not None and password:
            self.user_cache = Auth.authenticate(username=username, password=password)
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data


class AddUser(UserCreationForm):

    class Meta:
        model = User

        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'second_last_name',
            'is_staff',

        ]

        widgets = {

            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'second_last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'is_staff': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }


class EditUser(forms.ModelForm):

    class Meta:
        model = User

        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'second_last_name',
            'is_staff',
            'is_superuser',

        ]

        widgets = {

            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'second_last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'is_staff': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_superuser': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }