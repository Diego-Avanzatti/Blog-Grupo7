from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView, ListView, DetailView
from apps.Comment.models import Comment


class HomeView(TemplateView):
    template_name = 'comentario.html'

class CrearComentario(CreateView):
    model = Comment
    fields = ['usuario', 'post', 'texto', 'fecha']
    template_name = 'agregar_comentario.html'
    success_url = reverse_lazy('comentario.html')


class ActualizarComentario(UpdateView):
    model = Comment
    fields = ['usuario', 'post', 'texto', 'fecha']
    template_name = 'actualizar_comentario.html'
    success_url = reverse_lazy('comentario.html')


class EliminarComentario(DeleteView):
    model = Comment
    template_name = 'confirma_eliminar_comentario.html'
    success_url = reverse_lazy('comentario.html')


class ListarComentario(ListView):
    model = Comment
    template_name = 'listar_comentario.html'
    context_object_name = 'comentario'


    def get_context_data(self):
        context = super().get_context_data()
        comentario = Comment.objects.all()
        context['comentario'] = comentario


    def get_queryset(self):
        query = self.request.GET.get('buscador')
        queryset = super().get_queryset()


        if query:
            queryset = queryset.filter(nombre__icontains = query)
        return queryset.order_by('post')
