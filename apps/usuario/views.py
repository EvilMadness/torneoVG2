from django.contrib.auth import login, logout
from apps.usuario.models import User
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from sweetify.views import SweetifySuccessMixin
from sweetify import *

from apps.usuario.forms import LoginForm, AddUser, EditUser, ResetForm, ResetConfirmForm


def index(request):
    return render(request, 'usuario/index.html')


class Login(LoginView):
    form_class = LoginForm
    template_name = 'usuario/login.html'
    success_url = reverse_lazy('home:index')

    def form_valid(self, form):
        login(self.request, form.get_user())
        info(self.request, 'Bienvenido(a) '+str(self.request.user.username)+'!', toast=True, position='top', timer=2500)
        return HttpResponseRedirect(self.success_url)


class Logout(LogoutView):
    success_url = reverse_lazy('usuario:login')

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        success_url = self.success_url
        if success_url:
            # Redirect to this page until the session has been cleared.
            return HttpResponseRedirect(success_url)
        return super().dispatch(request, *args, **kwargs)


def index(request):
    usuario = User.objects.all()
    return render(request, 'usuario/index.html', {'object_list': usuario})


class ShowUser(ListView):
    model = User
    template_name = 'usuario/table.html'



class RegisterUser(CreateView):
    model = User
    form_class = AddUser
    template_name = 'usuario/add_usuario.html'
    success_url = reverse_lazy('usuario:index')


class UpdateUser(UpdateView):
    model = User
    form_class = EditUser
    template_name = 'usuario/edit_user.html'
    success_url = reverse_lazy('usuario:index')
    context_object_name = 'usuario'


class DeleteUser(DeleteView):
    model = User
    template_name = 'usuario/delete_user.html'
    success_url = reverse_lazy('usuario:index')


class Table(ListView):
    model = User
    template_name = 'usuario/table.html'
    paginate_by = 2


class Reset(SweetifySuccessMixin, PasswordResetView):
    template_name = "restaurar_pass/password_reset_form.html"
    email_template_name = "restaurar_pass/password_reset_email.html"
    form_class = ResetForm
    sweetify_options = {'toast': True, 'position': 'top', 'timer': 2500}
    success_message = 'Correo enviado correctamente.!'
    success_url = reverse_lazy('usuario:password_reset_done')


class ResetDone(PasswordResetDoneView):
    template_name = "restaurar_pass/password_reset_done.html"


class ResetConfirm(SweetifySuccessMixin, PasswordResetConfirmView):
    template_name = "restaurar_pass/password_reset_confirm.html"
    form_class = ResetConfirmForm
    sweetify_options = {'toast': True, 'position': 'top', 'timer': 2500}
    success_message = 'Contraseña restablecida correctamente!'
    success_url = reverse_lazy('usuario:password_reset_complete')


class ResetComplete(PasswordResetCompleteView):
    template_name = "restaurar_pass/password_reset_complete.html"