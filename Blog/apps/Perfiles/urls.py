from django.urls import path
from .views import SignUpView, UsuarioView, AdminView
from .views import Login

app_name = 'apps.Perfiles'

urlpatterns = [
    path("usuario/", UsuarioView.as_view(), name="usuario"),
    path("admin/", AdminView.as_view(), name="admin"),
    path('registrarse/',SignUpView.as_view(), name='registrarse'),
    path('login/',Login.as_view(), name='login'),
]


