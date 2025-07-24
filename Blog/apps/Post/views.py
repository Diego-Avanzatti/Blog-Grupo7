from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from .models import Post, Genero, Plataforma

# ----- Género ------

class AgregarGenero(CreateView):
    model = Genero
    fields= ['genero']
    template_name = 'posts/genero/agregar_genero.html'
    success_url = reverse_lazy('apps.Perfiles:admin')

class ActualizarGenero(UpdateView):
    model = Genero
    fields= ['genero']
    template_name = 'posts/genero/actualizar_genero.html'
    success_url = reverse_lazy('apps.Perfiles:admin')

class EliminarGenero(DeleteView):
    model = Genero
    template_name = 'posts/genero/confirma_eliminar_genero.html'
    success_url = reverse_lazy('apps.Perfiles:admin')


# ----- Plataforma ------

class AgregarPlataforma(CreateView):
    model = Plataforma
    fields= ['plataforma']
    template_name = 'posts/plataforma/agregar_plataforma.html'
    success_url = reverse_lazy('apps.Perfiles:admin')

class ActualizarPlataforma(UpdateView):
    model = Plataforma
    fields= ['plataforma']
    template_name = 'posts/plataforma/actualizar_plataforma.html'
    success_url = reverse_lazy('apps.Perfiles:admin')

class EliminarPlataforma(DeleteView):
    model = Plataforma
    template_name = 'posts/plataforma/confirma_eliminar_plataforma.html'
    success_url = reverse_lazy('apps.Perfiles:admin')


# ----- Post ------

class CrearPost(CreateView):
    model = Post
    fields = [
        'titulo', 'subtitulo', 'fecha', 
        'descripcion', 'genero', 'plataforma',
        'activo', 'imagen_post'
        ]
    template_name = 'posts/agregar_post.html'
    success_url = reverse_lazy('apps.Perfiles:admin')


class ActualizarPost(UpdateView):
    model = Post
    fields = [
        'titulo', 'subtitulo', 'fecha', 
        'descripcion', 'genero', 'plataforma',
        'activo', 'imagen_post'
        ]
    template_name = 'posts/actualizar_post.html'
    success_url = reverse_lazy('apps.Perfiles:admin')


class EliminarPost(DeleteView):
    model = Post
    template_name = 'posts/confirma_elimina_post.html'
    success_url = reverse_lazy('apps.Perfiles:admin')


# ----- Post(inicio) ------


class ListarPost(ListView):
    model = Post
    template_name = 'posts/post.html'
    context_object_name = 'post'


    def get_context_data(self):
        context = super().get_context_data()
        posts = Post.objects.all()
        context['posts'] = posts
        return context 


    def get_queryset(self):
        query = self.request.GET.get('buscador')
        queryset = super().get_queryset()


        if query:
            queryset = queryset.filter(nombre__icontains = query)
        return queryset.order_by('titulo')
    

class DetallarPost(DetailView):
    model = Post
    template_name = 'posts/post_individual.html'
    context_object_name = 'post'
    pk_url_kwarg = 'id'
    queryset = Post.objects.all()


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comentarios'] = self.object.comentarios.all().order_by('-fecha')
        return context



