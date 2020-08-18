from django.contrib import admin
from .models import Categoria, Post

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)
