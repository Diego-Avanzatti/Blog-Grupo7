from django.urls import path
from .views import CrearPost, ActualizarPost, EliminarPost, ListarPost , DetallarPost
from .views import AgregarGenero, ActualizarGenero, EliminarGenero
from .views import AgregarPlataforma, ActualizarPlataforma, EliminarPlataforma


app_name = 'post'

urlpatterns = [
    path("agregar_genero/", AgregarGenero.as_view(), name="agregar_genero"),
    path("actualizar_genero/", ActualizarGenero.as_view(), name="actualizar_genero"),
    path("eliminar_genero/", EliminarGenero.as_view(), name="eliminar_genero"),

    path("agregar_plataforma/", AgregarPlataforma.as_view(), name="agregar_plataforma"),
    path("actualizar_plataforma/", ActualizarPlataforma.as_view(), name="actualizar_plataforma"),
    path("eliminar_plataforma/", EliminarPlataforma.as_view(), name="eliminar_plataforma"),

    path('', ListarPost.as_view(),name='posts'),
    path('agregar/', CrearPost.as_view(),name='agregar_post'),
    path('actualizar/<int:pk>/', ActualizarPost.as_view(), name='actualizar_post'),
    path('eliminar/<int:pk>',EliminarPost.as_view(),name='eliminar_post'),
    path('<int:id>/',DetallarPost.as_view(),name='post_individual'),
]