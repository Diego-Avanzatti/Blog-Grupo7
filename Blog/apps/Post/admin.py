from django.contrib import admin
from .models import Genero, Plataforma, Post

class GeneroAdmin(admin.ModelAdmin):
    list_display = ('id', 'genero')

class PlataformaAdmin(admin.ModelAdmin):
    list_display = ('id', 'plataforma')

class PostAdmin(admin.ModelAdmin):
    list_display = ('id','titulo', 'subtitulo', 'fecha', 'descripcion', 'imagen_post', 'genero', 'plataforma', 'activo')

admin.site.register(Genero, GeneroAdmin)
admin.site.register(Plataforma, PlataformaAdmin)
admin.site.register(Post, PostAdmin)
