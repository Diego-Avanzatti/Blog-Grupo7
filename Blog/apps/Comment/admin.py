from django.contrib import admin
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'post', 'texto', 'fecha')

admin.site.register(Comment, CommentAdmin)
