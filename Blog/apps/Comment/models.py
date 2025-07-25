from django.db import models
from apps.Post.models import Post
from django.contrib.auth.models import User

class Comment(models.Model):
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='comentarios')
    texto = models.TextField()
    fecha = models.DateTimeField(auto_created=True)

    def __str__(self):
        return f'Comentario: {self.usuario.username} - {self.post.titulo}.'
    
