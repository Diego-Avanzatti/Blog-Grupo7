from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView, ListView, DetailView
from apps.Post.models import Post


class HomeView(TemplateView):
    template_name = 'post.html'

class CrearPost(CreateView):
    model = Post
    fields = [
        'titulo', 'subtitulo', 'fecha', 
        'descripcion', 'genero', 'plataforma',
        'activo', 'imagen_post'
        ]
    template_name = 'agregar_post.html'
    success_url = reverse_lazy('post.html')


class ActualizarPost(UpdateView):
    model = Post
    fields = [
        'titulo', 'subtitulo', 'fecha', 
        'descripcion', 'genero', 'plataforma',
        'activo', 'imagen_post'
        ]
    template_name = 'actualizar_post.html'
    success_url = reverse_lazy('post.html')


class EliminarPost(DeleteView):
    model = Post
    template_name = 'confirma_eliminar_post.html'
    success_url = reverse_lazy('post.html')


class ListarPost(ListView):
    model = Post
    template_name = 'listar_post.html'
    context_object_name = 'posts'


    def get_context_data(self):
        context = super().get_context_data()
        posts = Post.objects.all()
        context['posts'] = posts


    def get_queryset(self):
        query = self.request.GET.get('buscador')
        queryset = super().get_queryset()


        if query:
            queryset = queryset.filter(nombre__icontains = query)
        return queryset.order_by('titulo')