from django.urls import path
from .views import HomeView, CrearPost, ActualizarPost, EliminarPost, ListarPost

urlpatterns = [
    path('post/', HomeView.as_view(),name='post'),
    path('agregar_post/', CrearPost.as_view(),name='agregar_post'),
    path('actualizar_post/', ActualizarPost.as_view(),name='actualizar_post'),
    path('listar_post/', ListarPost.as_view(),name='listar_post'),
    path('eliminar_post/<int:pk>',EliminarPost.as_view(),name='eliminar_post'),
]