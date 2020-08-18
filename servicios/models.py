from django.db import models

class Servicio(models.Model):
    titulo = models.CharField('Titulo', max_length=50)
    contenido = models.CharField('Contenido', max_length=50)
    imagem = models.ImageField('Imagem', upload_to='servicios')
    created_at = models.DateField('Criado em', auto_now_add = True)
    updated_at = models.DateField('Atualizado em', auto_now = True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name  = 'Servicio'
        verbose_name_plural  = 'Servicios'
    

