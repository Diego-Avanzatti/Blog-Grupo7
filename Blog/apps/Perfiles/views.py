from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import SignUpForm
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

class UsuarioView(TemplateView):
    template_name = 'perfiles/usuario.html'

class AdminView(TemplateView):
    template_name = 'perfiles/usuario.html'


# ----------registrar usuarios----------

class SignUpView(FormView):
    template_name = 'perfiles/registrarse.html'
    form_class = SignUpForm
    success_url = reverse_lazy('apps.Perfiles:login')


    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    

#----------Login---------------------


class Login(auth_views.LoginView):
    template_name = 'perfiles/login.html'