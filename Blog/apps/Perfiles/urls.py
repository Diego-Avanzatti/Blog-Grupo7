from django.urls import path
from .views import Perfil

urlpatterns = [
    path('perfil/',Perfil.as_view(), name='perfil')
]


