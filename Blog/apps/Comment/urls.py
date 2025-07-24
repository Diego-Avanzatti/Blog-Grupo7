from django.urls import path
from .views import CrearComentario, ActualizarComentario, EliminarComentario, ListarComentario

apps_name = 'comentario'

urlpatterns = [
    path('', ListarComentario.as_view(),name='comentario'),
    path('agregar/', CrearComentario.as_view(),name='agregar_comentario'),
    path('actualizar/', ActualizarComentario.as_view(),name='actualizar_comentario'),
    path('eliminar/<int:id>',EliminarComentario.as_view(),name='eliminar_comentario'),
]