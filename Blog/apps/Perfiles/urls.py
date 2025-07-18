from django.urls import path
from .views import Perfil

urlpatterns = [
    path('',Perfil.as_view(), name='perfil')
]


