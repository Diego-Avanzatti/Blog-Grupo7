from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen_perfil = models.ImageField(upload_to='perfiles/', blank=True, null=True)
    biografia = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'Perfil de {self.usuario.username}'
    
    def delete(self, using = None, keep_parents = False):
        self.imagen_perfil.delete(self.imagen_perfil.name)
        super().delete()
