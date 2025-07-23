from django.contrib import admin
from .models import Perfil

class PerfilAdmin(admin.ModelAdmin):
    list_display = ('id','usuario', 'imagen_perfil', 'biografia')


admin.site.register(Perfil, PerfilAdmin)