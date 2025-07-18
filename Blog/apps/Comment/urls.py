from django.urls import path
from .views import HomeView, CrearComentario, ActualizarComentario, EliminarComentario, ListarComentario

urlpatterns = [
    path('', HomeView.as_view(),name='comentario'),
    path('agregar/', CrearComentario.as_view(),name='agregar_comentario'),
    path('actualizar/', ActualizarComentario.as_view(),name='actualizar_comentario'),
    path('listar/', ListarComentario.as_view(),name='listar_comentario'),
    path('eliminar/<int:pk>',EliminarComentario.as_view(),name='eliminar_comentario'),
]