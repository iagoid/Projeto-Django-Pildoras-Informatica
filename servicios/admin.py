from django.contrib import admin
from .models import Servicio

class ServicioAdmin(admin.ModelAdmin):
    fields = ('titulo', 'contenido', 'imagem')


admin.site.register(Servicio, ServicioAdmin)