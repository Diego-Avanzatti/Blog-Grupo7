from django.urls import path
from .views import HomeView, CrearComentario, ActualizarComentario, EliminarComentario, ListarComentario

urlpatterns = [
    path('comentario/', HomeView.as_view(),name='comentario'),
    path('agregar_comentario/', CrearComentario.as_view(),name='agregar_comentario'),
    path('actualizar_comentario/', ActualizarComentario.as_view(),name='actualizar_comentario'),
    path('listar_comentario/', ListarComentario.as_view(),name='listar_comentario'),
    path('eliminar_comentario/<int:pk>',EliminarComentario.as_view(),name='eliminar_comentario'),
]