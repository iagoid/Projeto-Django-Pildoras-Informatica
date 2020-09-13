from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    nombre = models.CharField('Titulo', max_length=50)
    created_at = models.DateField('Criado em', auto_now_add=True)
    updated_at = models.DateField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'


class Post(models.Model):
    titulo = models.CharField('Titulo', max_length=50)
    contenido = models.CharField('Contenido', max_length=50)
    imagem = models.ImageField(
        'Imagem', upload_to='blog', null=True, blank=True)
    autor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='Autor')
    categorias = models.ManyToManyField(Categoria, related_name='categorias')

    created_at = models.DateField('Criado em', auto_now_add=True)
    updated_at = models.DateField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
