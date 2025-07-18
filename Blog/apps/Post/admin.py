from django.contrib import admin
from .models import Genero, Plataforma, Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'subtitulo', 'fecha', 'descripcion', 'imagen_post', 'genero', 'plataforma', 'activo')

admin.site.register(Genero)
admin.site.register(Plataforma)
admin.site.register(Post, PostAdmin)
